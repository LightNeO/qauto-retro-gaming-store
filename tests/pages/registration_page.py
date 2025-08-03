from tests.pages.base_page import BasePage
from tests.locators import registration_page_locators, login_page_locators
from tests.test_data import registration_page_test_data


class RegistrationPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_registration_page(self):
        self.page.goto(self.base_url)
        self.wait_for_page_load()

    def fill_username(self, username):
        self.fill_element(registration_page_locators.USERNAME_FIELD, username)

    def fill_email(self, email):
        self.fill_element(registration_page_locators.EMAIL_FIELD, email)

    def fill_password(self, password):
        self.fill_element(registration_page_locators.PASSWORD_FIELD, password)

    def click_register_button(self):
        self.click_element(registration_page_locators.REGISTER_BUTTON)

    def register(self, username, email, password):
        self.fill_username(username)
        self.fill_email(email)
        self.fill_password(password)
        self.click_register_button()

    def register_with_existing_username(self, email, password):
        self.register(registration_page_test_data.EXISTING_USERNAME, email, password)

    def register_with_existing_email(self, username, password):
        self.register(username, registration_page_test_data.EXISTING_EMAIL, password)

    def register_with_valid_data(self):
        self.register(
            registration_page_test_data.get_random_username(),
            registration_page_test_data.get_random_email(),
            registration_page_test_data.get_random_password(),
        )

    def register_with_empty_username(self, email, password):
        self.register("", email, password)

    def register_with_empty_email(self, username, password):
        self.register(username, "", password)

    def register_with_empty_password(self, username, email):
        self.register(username, email, "")

    def register_with_invalid_email_format(self, username, invalid_email, password):
        self.register(username, invalid_email, password)

    def get_registration_message(self):
        return self.get_element_text(registration_page_locators.REGISTRATION_MESSAGE)

    def get_username_field_value(self):
        return self.get_field_value(registration_page_locators.USERNAME_FIELD)

    def get_email_field_value(self):
        return self.get_field_value(registration_page_locators.EMAIL_FIELD)

    def get_password_field_value(self):
        return self.get_field_value(registration_page_locators.PASSWORD_FIELD)

    def is_username_field_valid(self):
        return self.is_field_valid(registration_page_locators.USERNAME_FIELD)

    def is_email_field_valid(self):
        return self.is_field_valid(registration_page_locators.EMAIL_FIELD)

    def is_password_field_valid(self):
        return self.is_field_valid(registration_page_locators.PASSWORD_FIELD)

    def clear_username_field(self):
        self.clear_field(registration_page_locators.USERNAME_FIELD)

    def clear_email_field(self):
        self.clear_field(registration_page_locators.EMAIL_FIELD)

    def clear_password_field(self):
        self.clear_field(registration_page_locators.PASSWORD_FIELD)

    def expect_title_to_be_visible(self):
        self.expect_element_to_be_visible(
            registration_page_locators.REGISTRATION_PAGE_TITLE
        )

    def expect_username_field_to_be_visible(self):
        self.expect_element_to_be_visible(registration_page_locators.USERNAME_FIELD)

    def expect_email_field_to_be_visible(self):
        self.expect_element_to_be_visible(registration_page_locators.EMAIL_FIELD)

    def expect_password_field_to_be_visible(self):
        self.expect_element_to_be_visible(registration_page_locators.PASSWORD_FIELD)

    def expect_register_button_to_be_visible(self):
        self.expect_element_to_be_visible(registration_page_locators.REGISTER_BUTTON)

    def expect_already_have_account_link_to_be_visible(self):
        self.expect_element_to_be_visible(
            registration_page_locators.ALREADY_HAVE_AN_ACCOUNT_LINK
        )

    def expect_title_to_have_text(self, text):
        self.expect_element_to_have_text(
            registration_page_locators.REGISTRATION_PAGE_TITLE, text
        )

    def expect_registration_message_to_contain_text(self, text):
        self.expect_element_to_contain_text(
            registration_page_locators.REGISTRATION_MESSAGE, text
        )

    def expect_username_field_to_have_value(self, value):
        self.expect_element_to_have_value(
            registration_page_locators.USERNAME_FIELD, value
        )

    def expect_email_field_to_have_value(self, value):
        self.expect_element_to_have_value(registration_page_locators.EMAIL_FIELD, value)

    def expect_password_field_to_have_value(self, value):
        self.expect_element_to_have_value(
            registration_page_locators.PASSWORD_FIELD, value
        )

    def verify_redirected_to_login_page(self):
        self.wait_for_element(login_page_locators.LOGIN_FORM)
        login_page_title = self.get_element_text(login_page_locators.TITLE)
        return login_page_title == "Login"

    def get_page_title_text(self):
        return self.get_element_text(registration_page_locators.REGISTRATION_PAGE_TITLE)
