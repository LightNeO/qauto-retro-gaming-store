from tests.pages.base_page import BasePage
from tests.locators import registration_page_locators


class RegistrationPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_registration_page(self):
        self.page.goto(self.base_url)

    def wait_for_main_content(self, timeout=10000):
        self.wait_for_element("body", timeout)
