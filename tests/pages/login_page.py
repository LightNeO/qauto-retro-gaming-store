from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_login_page(self):
        self.page.goto(self.base_url)
