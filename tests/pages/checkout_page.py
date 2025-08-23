from .base_page import BasePage
from ..locators import checkout_page_locators
from ..test_data import checkout_page_test_data


class CheckoutPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.page = page
        self.base_url = base_url

    def navigate_to_checkout_page(self):
        """Navigate to the checkout page"""
        self.page.goto(f"{self.base_url}/checkout")
        self.wait_for_page_load()

    def expect_checkout_page_loaded(self):
        """Verify checkout page is loaded correctly"""
        self.expect_element_to_be_visible(checkout_page_locators.CHECKOUT_PAGE_TITLE)
