from faker import Faker

fake = Faker()


def get_random_username():
    """Generate a random username for testing"""
    return fake.user_name()


def get_random_password():
    """Generate a random password for testing"""
    return fake.password(
        length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
    )


PERFORMANCE_THRESHOLD_MS = 10000
EXPECTED_TITLE = "Login"
EXPECTED_ERROR_MESSAGE = "No active account found with the given credentials"
EXPECTED_SUCCESS_MESSAGE = "Login successful! Redirecting..."
INVALID_USERNAME = "q"
INVALID_PASSWORD = "q"
EMPTY_USERNAME = ""
EMPTY_PASSWORD = ""
EXISTING_USERNAME = "testuser123"
VALID_PASSWORD = "Test@123"
