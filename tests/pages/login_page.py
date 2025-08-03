from tests.pages.base_page import BasePage
from tests.locators import login_page_locators, homepage_locators
from tests.test_data import login_page_test_data


class LoginPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_login_page(self):
        self.page.goto(self.base_url)
        self.wait_for_page_load()

    def fill_username(self, username):
        self.fill_element(login_page_locators.USERNAME_FIELD, username)

    def fill_password(self, password):
        self.fill_element(login_page_locators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_element(login_page_locators.LOGIN_BUTTON)

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()

    def login_with_invalid_data(self):
        self.login(
            login_page_test_data.INVALID_USERNAME, login_page_test_data.INVALID_PASSWORD
        )

    def login_with_existing_user(self):
        self.login(
            login_page_test_data.EXISTING_USERNAME, login_page_test_data.VALID_PASSWORD
        )

    def login_with_empty_username(self, password):
        self.login(login_page_test_data.EMPTY_USERNAME, password)

    def login_with_empty_password(self, username):
        self.login(username, login_page_test_data.EMPTY_PASSWORD)

    def logout(self):
        logout_menu_item = self.get_element(homepage_locators.LOGOUT_MENU_ITEM)
        logout_menu_item.click()

    def get_login_message(self):
        return self.get_element_text(login_page_locators.LOGIN_MESSAGE)

    def get_username_field_value(self):
        return self.get_field_value(login_page_locators.USERNAME_FIELD)

    def get_password_field_value(self):
        return self.get_field_value(login_page_locators.PASSWORD_FIELD)

    def is_username_field_valid(self):
        return self.is_field_valid(login_page_locators.USERNAME_FIELD)

    def is_password_field_valid(self):
        return self.is_field_valid(login_page_locators.PASSWORD_FIELD)

    def clear_username_field(self):
        self.clear_field(login_page_locators.USERNAME_FIELD)

    def clear_password_field(self):
        self.clear_field(login_page_locators.PASSWORD_FIELD)

    def expect_title_to_be_visible(self):
        self.expect_element_to_be_visible(login_page_locators.TITLE)

    def expect_username_field_to_be_visible(self):
        self.expect_element_to_be_visible(login_page_locators.USERNAME_FIELD)

    def expect_password_field_to_be_visible(self):
        self.expect_element_to_be_visible(login_page_locators.PASSWORD_FIELD)

    def expect_login_button_to_be_visible(self):
        self.expect_element_to_be_visible(login_page_locators.LOGIN_BUTTON)

    def expect_title_to_have_text(self, text):
        self.expect_element_to_have_text(login_page_locators.TITLE, text)

    def expect_login_message_to_have_text(self, text):
        self.expect_element_to_have_text(login_page_locators.LOGIN_MESSAGE, text)

    def expect_username_field_to_have_value(self, value):
        self.expect_element_to_have_value(login_page_locators.USERNAME_FIELD, value)

    def expect_password_field_to_have_value(self, value):
        self.expect_element_to_have_value(login_page_locators.PASSWORD_FIELD, value)

    def verify_jwt_token_stored(self):
        storage_state = self.page.context.storage_state()
        jwt_token_found = False
        origins = storage_state.get("origins", [])

        for origin_data in origins:
            localStorage = origin_data.get("localStorage", [])
            for item in localStorage:
                if item.get("name") in ["token", "refresh"]:
                    jwt_token_found = True
                    break
            if jwt_token_found:
                break

        return jwt_token_found

    def verify_jwt_token_cleared(self):
        storage_state = self.page.context.storage_state()
        return not storage_state.get("origins", [])

    def verify_user_logged_in(self):
        return self.is_element_visible(
            homepage_locators.PROFILE_MENU_ITEM
        ) and self.is_element_visible(homepage_locators.LOGOUT_MENU_ITEM)

    def verify_user_logged_out(self):
        return self.is_element_visible(
            homepage_locators.LOGIN_MENU_ITEM
        ) and self.is_element_visible(homepage_locators.REGISTER_MENU_ITEM)
