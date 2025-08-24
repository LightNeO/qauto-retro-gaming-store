from tests.test_data import checkout_page_test_data
import pytest


class TestCheckoutPage:

    @pytest.mark.smoke
    def test_checkout_page_loads_with_cart_items(self, checkout_page_with_cart):
        """
        TC-001: Verify checkout page loads correctly with items in cart

        Steps:
        1. Navigate to checkout page with user logged in and product in cart
        2. Verify checkout page loads correctly
        """
        checkout_page = checkout_page_with_cart

        # Verify page loads correctly
        checkout_page.expect_checkout_page_loaded()
