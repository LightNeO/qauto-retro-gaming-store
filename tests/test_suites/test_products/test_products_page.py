import pytest
from tests.test_data import products_page_test_data
from tests.utils.performance_helper import PerformanceHelper


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
    2. Verify products grid has correct number of products(static value that is in the test data)
    """
    products_page.navigate_to_products_page()
    products_page.expect_correct_amount_of_products(
        products_page_test_data.EXPECTED_NUMBER_OF_PRODUCTS
    )


@pytest.mark.fail_expected
def test_verify_all_product_images_are_visible(products_page):
    """
    TC-050: Verify all product images are visible

    Steps:
    1. Navigate to products page
    2. Verify all product images are visible
    """
    products_page.navigate_to_products_page()
    products_page.expect_all_product_images_to_be_visible()


@pytest.mark.smoke
def test_verify_search_bar_is_visible(products_page):
    """
    TC-051: Verify search bar is visible

    Steps:
    1. Navigate to products page
    2. Verify search bar is visible
    """
    products_page.navigate_to_products_page()
    products_page.expect_search_bar_to_be_visible()


@pytest.mark.smoke
def test_verify_search_button_is_visible(products_page):
    """
    TC-052: Verify search button is visible

    Steps:
    1. Navigate to products page
    2. Verify search button is visible
    """
    products_page.navigate_to_products_page()
    products_page.expect_search_button_to_be_visible()


@pytest.mark.smoke
def test_verify_sort_dropdown_is_visible(products_page):
    """
    TC-053: Verify sort dropdown is visible

    Steps:
    1. Navigate to products page
    2. Verify sort dropdown is visible
    """
    products_page.navigate_to_products_page()
    products_page.expect_sort_dropdown_to_be_visible()


@pytest.mark.test
def test_verify_search_works_with_valid_product_name(products_page):
    """
    TC-054: Verify search works with valid product name

    Steps:
    1. Navigate to products page
    2. Search for a valid product name
    3. Verify search results are visible
    """
    products_page.navigate_to_products_page()
    products_page.search_for_product(products_page_test_data.VALID_PRODUCT_NAME)
    all_products_titles = products_page.get_all_products_titles()
    for product_title in all_products_titles:
        assert (
            products_page_test_data.VALID_PRODUCT_NAME in product_title.text_content().lower()
        )


@pytest.mark.test
def test_verify_search_with_invalid_product_name(products_page):
    """
    TC-055: Verify search works with invalid product name

    Steps:
    1. Navigate to products page
    2. Search for an invalid product name
    3. Verify no search results are visible
    """
    products_page.navigate_to_products_page()
    products_page.search_for_product(products_page_test_data.INVALID_PRODUCT_NAME)
    products_page.expect_no_results_message_to_be_visible()
