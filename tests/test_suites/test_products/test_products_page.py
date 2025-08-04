import pytest
from tests.test_data import products_page_test_data
from tests.locators import products_page_locators
from tests.utils.performance_helper import PerformanceHelper
from playwright.sync_api import expect


@pytest.mark.smoke
def test_products_page_loads_within_10_seconds(products_page):
    """
    TC-046: Verify products page loads within 10 seconds
    """
    PerformanceHelper.assert_page_loads_within_threshold(
        products_page,
        products_page.navigate_to_products_page,
        products_page_test_data.PERFORMANCE_THRESHOLD_MS,
        "Products page",
    )


@pytest.mark.smoke
def test_products_page_has_correct_title(products_page):
    """
    TC-047: Verify products page has correct title

    Steps:
    1. Navigate to products page
    2. Verify title is visible
    3. Verify title has correct text
    """
    products_page.navigate_to_products_page()
    products_page.expect_title_to_be_visible()
    products_page.expect_title_to_have_text(products_page_test_data.TITLE)


@pytest.mark.smoke
def test_grid_is_visible(products_page):
    """
    TC-048: Verify products grid is visible

    Steps:
    1. Navigate to products page
    2. Verify products grid is visible
    """
    products_page.navigate_to_products_page()
    products_page.expect_products_grid_to_be_visible()


@pytest.mark.smoke
def test_grid_has_correct_number_of_products(products_page):
    """
    TC-049: Verify products grid has correct number of products

    Steps:
    1. Navigate to products page
    2. Verify products grid has correct number of products
    """
    products_page.navigate_to_products_page()
    products_page.expect_correct_amount_of_products(
        products_page_test_data.EXPECTED_NUMBER_OF_PRODUCTS
    )


@pytest.mark.test
def test_verify_all_product_images_are_visible(products_page):
    """
    TC-050: Verify all product images are visible

    Steps:
    1. Navigate to products page
    2. Verify all product images are visible
    """
    products_page.navigate_to_products_page()
    products_page.expect_all_product_images_to_be_visible()
