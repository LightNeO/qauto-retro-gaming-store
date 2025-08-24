import pytest

from tests.locators import checkout_page_locators


class TestCheckoutPage:

    @pytest.mark.smoke
    def test_checkout_page_loads_with_cart_items(self, checkout_page_with_cart):
        """
        TC-077: Verify checkout page loads correctly

        Steps:
        1. Navigate to checkout page with user logged in and product in cart
        2. Verify checkout page loads correctly
        """
        checkout_page = checkout_page_with_cart

        # Verify page loads correctly
        checkout_page.expect_checkout_page_loaded()

    @pytest.mark.smoke
    def test_visibility_of_checkout_elements(self, checkout_page_with_cart):
        """
        TC-078: Verify checkout elements are visible

        Steps:
        1. Navigate to checkout page with user logged in and product in cart
        2. Verify all checkout elements are visible
        """
        checkout_page_with_cart.navigate_to_checkout_page()
        checkout_page_with_cart.expect_all_checkout_elements_to_be_visible()

    @pytest.mark.test
    def test_name_field_is_mandatory(self, checkout_page_with_cart):
        """
        TC-079: Verify name field is mandatory

        Steps:
        1. Navigate to checkout page with user logged in and product in cart
        2. Fill all fields with valid infor
        3. Leave name field empty
        4. Click the "Place order" button
        5. Verify error for name field
        """
        checkout_page_with_cart.navigate_to_checkout_page()
        checkout_page_with_cart.fill_all_fields_with_valid_data()
        checkout_page_with_cart.clear_field(checkout_page_locators.FULL_NAME_FIELD)
        checkout_page_with_cart.click_element(checkout_page_locators.PLACE_ORDER_BUTTON)
        assert not checkout_page_with_cart.expect_field_to_be_valid(
            checkout_page_locators.FULL_NAME_FIELD
        ), f"Field {checkout_page_locators.FULL_NAME_FIELD} should be invalid"
