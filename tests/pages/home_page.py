from tests.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_homepage(self):
        self.page.goto(self.base_url)

    def wait_for_main_content(self, timeout=10000):
        from tests.locators import homepage_locators
        self.wait_for_element(homepage_locators.MAIN_CONTENT, timeout)
