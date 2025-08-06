import pytest
from tests.test_data.product_detail_page_test_data import PERFORMANCE_THRESHOLD_MS
from tests.utils.performance_helper import PerformanceHelper


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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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
