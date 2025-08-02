from tests.pages.base_page import BasePage
from tests.locators import login_page_locators, homepage_locators
from tests.test_data import login_page_test_data


class LoginPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_login_page(self):
        self.page.goto(self.base_url)

    def login(self, username, password):
        login_field = self.get_element(login_page_locators.USERNAME_FIELD)
        login_field.fill(username)
        password_field = self.get_element(login_page_locators.PASSWORD_FIELD)
        password_field.fill(password)
        login_button = self.get_element(login_page_locators.LOGIN_BUTTON)
        login_button.click()

    def login_with_invalid_data(self):
        self.login(
            login_page_test_data.INVALID_USERNAME, login_page_test_data.INVALID_PASSWORD
        )

    def login_with_existing_user(self):
        self.login(
            login_page_test_data.EXISTING_USERNAME, login_page_test_data.VALID_PASSWORD
        )

    def logout(self):
        logout_menu_item = self.get_element(homepage_locators.LOGOUT_MENU_ITEM)
        logout_menu_item.click()
