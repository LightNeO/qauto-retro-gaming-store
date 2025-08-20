import json
from typing import Dict, Optional, Tuple


class APIAuth:
    def __init__(
        self,
        base_url: str,
        login_paths: Optional[list] = None,
        username_field: str = "username",
        password_field: str = "password",
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.login_paths = login_paths or [
            "/api/auth/token/",  # Django SimpleJWT token obtain pair
            "/api/auth/token",   # without trailing slash
            "/api/login/",       # fallback legacy/session login if present
            "/api/login",
        ]
        self.username_field = username_field
        self.password_field = password_field

    def _extract_tokens(self, payload: Dict) -> Tuple[Optional[str], Optional[str]]:
        access_candidates = [
            payload.get("access"),
            payload.get("token"),
            payload.get("jwt"),
        ]
        refresh_candidates = [
            payload.get("refresh"),
            payload.get("refresh_token"),
        ]
        access = next((v for v in access_candidates if isinstance(v, str) and v), None)
        refresh = next((v for v in refresh_candidates if isinstance(v, str) and v), None)
        return access, refresh

    def login_and_build_storage_state(
        self,
        api_request_context,
        username: str,
        password: str,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict:
        request_headers = {"Content-Type": "application/json"}
        if headers:
            request_headers.update(headers)

        body = json.dumps({
            self.username_field: username,
            self.password_field: password,
        })

        last_error: Optional[str] = None
        for path in self.login_paths:
            response = api_request_context.post(path, data=body, headers=request_headers)
            if response.ok:
                data = response.json()
                access, refresh = self._extract_tokens(data)
                if not access and not refresh:
                    last_error = "Login API responded OK but did not include recognizable token fields"
                    continue

                origin = self.base_url
                local_storage_items = []
                if access:
                    local_storage_items.append({"name": "token", "value": access})
                if refresh:
                    local_storage_items.append({"name": "refresh", "value": refresh})

                return {
                    "cookies": [],
                    "origins": [
                        {
                            "origin": origin,
                            "localStorage": local_storage_items,
                        }
                    ],
                }

            else:
                last_error = f"{response.status} {response.status_text()}"

        error_message = last_error or "Login API request failed"
        raise AssertionError(f"API login failed: {error_message}. Tried paths: {', '.join(self.login_paths)}")

