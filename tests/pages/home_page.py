from tests.pages.base_page import BasePage
from tests.locators import homepage_locators


class HomePage(BasePage):

    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_homepage(self):
        self.page.goto(self.base_url)

    def wait_for_main_content(self, timeout=10000):
        self.wait_for_element(homepage_locators.MAIN_CONTENT, timeout)

    def get_button_hover_state(self, locator):
        return self.page.locator(locator).evaluate("el => el.matches(':hover')")
