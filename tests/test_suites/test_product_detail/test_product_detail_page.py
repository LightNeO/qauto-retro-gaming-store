import pytest
from tests.test_data.product_detail_page_test_data import PERFORMANCE_THRESHOLD_MS
from tests.utils.performance_helper import PerformanceHelper
from tests.locators import product_detail_page_locators
from tests.test_data import product_detail_page_test_data
from tests.pages.login_page import LoginPage
from tests.pages.home_page import HomePage
import time


class TestProductDetailPage:

    @pytest.mark.smoke
    def test_product_detail_page_loads_within_10_seconds(self, product_detail_page):
        """
        TC-059: Verify product detail page loads within 10 seconds

        Steps:
        1. Start timer
        2. Navigate to product detail page
        3. Wait for page to load (main content visible)
        4. Stop timer
        5. Verify load time is within 10 seconds
        """
        PerformanceHelper.assert_page_loads_within_threshold(
            product_detail_page,
            product_detail_page.navigate_to_random_product_detail_page,
            PERFORMANCE_THRESHOLD_MS,
            "Product Detail Page",
        )

    @pytest.mark.smoke
    def test_navigate_to_product_detail(self, product_detail_page):
        """
        TC-060: Verify navigating to product detail page

        Steps:
        1. Navigate to product detail page
        2. Verify page loaded correctly
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()

        assert product_detail_page.is_element_visible(
            "body"
        ), "Product detail page did not load correctly"

    @pytest.mark.smoke
    def test_back_to_products_navigation(self, product_detail_page):
        """
        TC-061: Verify back to products button navication

        Steps:
        1. Navigate to product detail page
        2. Click products button
        3. Verify navigation to products page
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.back_to_products()
        assert product_detail_page.is_element_visible(
            "body"
        ), "Products page did not load correctly"

    @pytest.mark.smoke
    def test_product_name_is_displayed(self, product_detail_page):
        """
        TC-062: Verify product name is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product name is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_product_name_to_be_visible()

    @pytest.mark.smoke
    def test_product_price_is_displayed(self, product_detail_page):
        """
        TC-063: Verify product price is displayed

        Steps:
        1. Navigate to product detail page
            2. Verify product price is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_product_price_to_be_visible()

    @pytest.mark.smoke
    def test_product_description_is_displayed(self, product_detail_page):
        """
        TC-064: Verify product description is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product description is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_product_description_to_be_visible()

    @pytest.mark.smoke
    def test_product_avarge_rating_is_displayed(self, product_detail_page):
        """
        TC-065: Verify product avarge rating is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product avarge rating is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_avarage_rating_to_be_visible()

    @pytest.mark.smoke
    def test_product_rating_count_is_displayed(self, product_detail_page):
        """
        TC-066: Verify product rating count is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product rating count is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_rating_count_to_be_visible()

    @pytest.mark.smoke
    def test_product_rating_stars_is_displayed(self, product_detail_page):
        """
        TC-067: Verify product rating stars is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product rating stars is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_rating_stars_to_be_visible()

    @pytest.mark.smoke
    def test_product_add_to_cart_button_is_displayed(self, product_detail_page):
        """
        TC-068: Verify product add to cart button is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product add to cart button is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_add_to_cart_button_to_be_visible()

    @pytest.mark.smoke
    def test_product_quantity_input_is_displayed(self, product_detail_page):
        """
        TC-069: Verify product quantity input is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product quantity input is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_quantity_input_to_be_visible()

    @pytest.mark.smoke
    def test_product_comment_input_is_displayed(self, product_detail_page):
        """
        TC-070: Verify product comment input is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product comment input is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_comment_input_to_be_visible()

    @pytest.mark.smoke
    def test_product_image_is_displayed(self, product_detail_page):
        """
        TC-071: Verify product image is displayed

        Steps:
        1. Navigate to product detail page
        2. Verify product image is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.expect_product_image_to_be_visible()

    @pytest.mark.smoke
    def test_add_to_cart_button_for_not_logged_in_user(self, product_detail_page):
        """
        TC-072: Verify add to cart button is not displayed for not logged in user

        Steps:
        1. Navigate to product detail page as not logged in user
        2. Click the add to cart button
        3. Verify that error message is displayed
        """
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        dialog_message = product_detail_page.check_error_message_after_click(
            product_detail_page_locators.ADD_TO_CART_BUTTON
        )
        assert (
            dialog_message
            == product_detail_page_test_data.EXPECTED_ERROR_MESSAGE_AFTER_CLICK_ADD_TO_CART_BUTTON
        ), f"Expected dialog message not found. Got: {dialog_message}"

    @pytest.mark.smoke
    def test_quantity_input_and_add_to_cart_functionality(
        self, product_detail_page, login_page, home_page
    ):
        """
        TC-073: Verify quantity input functionality

        Steps:
        1. Navigate to product detail page
        2. Verify quantity input is functional
        """
        login_page.navigate_to_login_page()
        login_page.login_with_existing_user()
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        new_value = product_detail_page.increase_quantity_and_return_new_value()
        product_detail_page.click_add_to_cart_button()
        home_page.click_menu_item("cart")
        product_detail_page.wait_for_page_load()
        cart_quantity = int(
            product_detail_page.get_element_attribute(
                product_detail_page_locators.PRODUCT_QUANTITY_IN_CART, "value"
            )
        )
        assert (
            cart_quantity == new_value
        ), f"Cart quantity is not correct. Got: {cart_quantity}"
        product_detail_page.click_element(
            product_detail_page_locators.REMOVE_FROM_CART_BUTTON
        )

    @pytest.mark.smoke
    def test_comment_posting_functionality(self, product_detail_page, login_page):
        """
        TC-074: Verify comment posting functionality

        Steps:
        1. Navigate to product detail page
        2. Verify comment posting is functional
        """
        product_detail_page.clear_all_comments()
        login_page.navigate_to_login_page()
        login_page.login_with_existing_user()
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.clear_all_comments()
        product_detail_page.expect_comment_input_to_be_visible()
        product_detail_page.fill_element(
            product_detail_page_locators.COMMENT_INPUT,
            product_detail_page_test_data.TEST_COMMENT,
        )
        product_detail_page.click_element(
            product_detail_page_locators.POST_COMMENT_BUTTON
        )
        comment_text = product_detail_page.get_element_text(
            product_detail_page_locators.FIRST_COMMENT_INPUT
        )
        assert (
            comment_text == product_detail_page_test_data.TEST_COMMENT
        ), f"Expected comment text '{product_detail_page_test_data.TEST_COMMENT}', but got '{comment_text}'"

    @pytest.mark.test
    def test_cart_total_price_is_displayed_correctly(
        self, product_detail_page, login_page, home_page
    ):
        """
        TC-075: Verify cart total price is displayed correctly

        Steps:
        1. Navigate to product detail page
        2. Add two products to cart
        3. Verify cart total price is displayed correctly
        """
        login_page.navigate_to_login_page()
        login_page.login_with_existing_user()
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.click_add_to_cart_button()
        product_detail_page.navigate_to_random_product_detail_page()
        product_detail_page.wait_for_page_load()
        product_detail_page.click_add_to_cart_button()
        home_page.click_menu_item("cart")
        product_detail_page.wait_for_page_load()
        expected_total_price = round(
            float(
                product_detail_page.get_element_text(
                    product_detail_page_locators.TOAL_PRICE_IN_CART
                ).replace("$", "")
            ),
            2,
        )
        actual_total_price = round(product_detail_page.sum_all_prices_in_cart(), 2)
        assert (
            expected_total_price == actual_total_price
        ), f"Expected total price {expected_total_price}, but got {actual_total_price}"
        product_detail_page.delete_all_products_from_cart()
