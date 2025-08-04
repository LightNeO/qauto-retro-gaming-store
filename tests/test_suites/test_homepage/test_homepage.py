from turtle import home
import pytest
from tests.test_data import homepage_test_data
from tests.locators import homepage_locators
from tests.utils.performance_helper import PerformanceHelper
from playwright.sync_api import expect


@pytest.mark.smoke
def test_homepage_loads_within_10_seconds(home_page):
    """
    TC-001: Verify homepage loads within 10 seconds

    Steps:
    1. Start timer
    2. Navigate to homepage
    3. Wait for page to load (main content visible)
    4. Stop timer
    5. Verify load time is within 10 seconds
    """
    PerformanceHelper.assert_page_loads_within_threshold(
        home_page,
        home_page.navigate_to_homepage,
        homepage_test_data.PERFORMANCE_THRESHOLD_MS,
        "Homepage",
    )


@pytest.mark.smoke
def test_homepage_displays_correct_title(home_page):
    """
    TC-002: Verify homepage displays correct page title

    Steps:
    1. Navigate to homepage
    2. Verify page has correct title
    """
    home_page.navigate_to_homepage()
    home_page.expect_page_title(homepage_test_data.EXPECTED_HOMEPAGE_TITLE)


@pytest.mark.smoke
def test_header_contains_expected_data(home_page):
    """
    TC-003: Verify header contains expected navigation items

    Steps:
    1. Navigate to homepage
    2. Get header text content
    3. Verify expected header data is present
    """
    home_page.navigate_to_homepage()
    header_text = home_page.get_header_text()
    # Clean whitespace and newlines
    header_text_clean = " ".join(header_text.split())

    for expected_item in homepage_test_data.EXPECTED_HEADER_DATA:
        assert (
            expected_item in header_text_clean
        ), f"Expected header item '{expected_item}' not found"


@pytest.mark.smoke
def test_menu_items_hover_effects(home_page):
    """
    TC-004: Verify menu items hover effects

    Steps:
    1. Navigate to homepage
    2. Hover over each menu item
    3. Verify hover effect is applied to each item
    """
    home_page.navigate_to_homepage()

    menu_items = home_page.get_menu_items()

    for locator, menu_name in menu_items:
        home_page.hover_menu_item(menu_name.lower())
        hover_state = home_page.get_hover_state_by_locator(locator)
        assert hover_state, f"{menu_name} menu hover effect not applied"


@pytest.mark.smoke
def test_menu_items_hover_effects_disappear(home_page):
    """
    TC-005: Verify menu items hover effects disappear

    Steps:
    1. Navigate to homepage
    2. Hover over each menu item
    3. Move mouse away from menu items
    4. Verify hover effects disappear
    """
    home_page.navigate_to_homepage()

    menu_items = home_page.get_menu_items()

    for locator, menu_name in menu_items:
        home_page.hover_menu_item(menu_name.lower())
        home_page.move_mouse_away()
        hover_state = home_page.get_hover_state_by_locator(locator)
        assert not hover_state, f"{menu_name} menu hover effect did not disappear"


@pytest.mark.smoke
def test_verify_footer_is_visible(home_page):
    """
    TC-006: Verify footer is visible

    Steps:
    1. Navigate to homepage
    2. Verify footer is visible
    """
    home_page.navigate_to_homepage()
    home_page.expect_footer_visible()


@pytest.mark.smoke
def test_verify_footer_sections(home_page):
    """
    TC-007: Verify footer sections are visible and contain expected data

    Steps:
    1. Navigate to homepage
    2. Verify footer sections are visible and contain expected data
    """
    home_page.navigate_to_homepage()
    footer_sections = home_page.get_footer_sections_text()
    for section in homepage_test_data.EXPECTED_FOOTER_SECTIONS:
        assert section in footer_sections, f"Footer section '{section}' not found"


@pytest.mark.smoke
def test_verify_footer_sections_quick_links_redirect(home_page):
    """
    TC-008: Verify footer sections quick links redirect to the correct page

    Steps:
    1. Navigate to homepage
    2. Click on each quick link
    3. Verify the page redirects to the correct page
    """
    home_page.navigate_to_homepage()
    footer_quick_links = home_page.get_footer_quick_links()
    expected_links_text = homepage_test_data.EXPECTED_FOOTER_QUICK_LINKS
    for link in footer_quick_links:
        link_text = home_page.get_element(link).get_attribute("href")
        assert (
            link_text in expected_links_text
        ), f"Link '{link_text}' not found in expected links"


@pytest.mark.smoke
def test_verify_social_media_icons_are_visible(home_page):
    """
    TC-009: Verify social media icons are visible

    Steps:
    1. Navigate to homepage
    2. Verify social media icons are visible
    """
    home_page.navigate_to_homepage()
    home_page.expect_social_media_icons_visible()


@pytest.mark.fail_expected
def test_verify_social_media_links_redirect(home_page):
    """
    TC-010: Verify social media links redirect to the correct page

    Steps:
    1. Navigate to homepage
    2. Click on each social media link
    3. Verify the page redirects to the correct page
    """
    home_page.navigate_to_homepage()
    social_media_links = home_page.get_social_media_links()
    expected_links_text = homepage_test_data.EXPECTED_SOCIAL_MEDIA_LINKS
    failed_links = []  # collect failed links

    for link in social_media_links:
        link_text = home_page.get_element(link).get_attribute("href")
        if link_text not in expected_links_text:
            failed_links.append(f"Link '{link_text}' is broken")

    try:
        assert failed_links == []
    except AssertionError:
        pytest.fail(
            "THIS IS EXPECTED \n"
            + "Social media links validation failed:\n"
            + "\n".join(failed_links)
            + "\n"
            + "THIS IS EXPECTED"
        )


@pytest.mark.smoke
def test_verify_homepage_displays_only_three_products(home_page):
    """
    TC-011: Verify homepage displays only three products

    Steps:
    1. Navigate to homepage
    2. Verify homepage displays only three products
    """
    home_page.navigate_to_homepage()
    expect(
        home_page.page.locator(f"{homepage_locators.PRODUCTS_SECTION} > div")
    ).to_have_count(3)


@pytest.mark.smoke
def test_verify_all_product_images_are_visible(home_page):
    """
    TC-012: Verify all product images are visible

    Steps:
    1. Navigate to homepage
    2. Get all product images
    3. Verify each image has proper dimensions (not broken)
    """
    home_page.navigate_to_homepage()
    home_page.expect_all_product_images_to_be_visible()


@pytest.mark.smoke
def test_view_details_buttons_hover_effects(home_page):
    """
    TC-013: Verify view details buttons hover effects

    Steps:
    1. Navigate to homepage
    2. Hover over each view details button
    3. Verify hover effect is applied to each button
    """
    home_page.navigate_to_homepage()
    view_details_buttons = home_page.get_all_view_details_buttons()
    for index, button in enumerate(view_details_buttons):
        home_page.hover_view_details_button(index)

        hover_state = home_page.get_hover_state_by_element(button)
        assert hover_state, f"View details button {index + 1} hover effect not applied"


@pytest.mark.smoke
def test_view_details_buttons_hover_effects_disappear(home_page):
    """
    TC-014: Verify view details buttons hover effects disappear

    Steps:
    1. Navigate to homepage
    2. Hover over each view details button
    3. Verify hover effect is applied to each button
    """
    home_page.navigate_to_homepage()
    view_details_buttons = home_page.get_all_view_details_buttons()
    for index, button in enumerate(view_details_buttons):
        home_page.hover_view_details_button(index)
        home_page.move_mouse_away()
        hover_state = home_page.get_hover_state_by_element(button)
        assert (
            not hover_state
        ), f"View details button {index + 1} hover effect did not disappear"


@pytest.mark.smoke
def test_verify_click_product_card_not_redirects_to_product_page(home_page):
    """
    TC-015: Verify click product card not redirects to product page

    Steps:
    1. Navigate to homepage
    2. Click on each product card
    3. Verify the page does not redirect to the product page
    """
    home_page.navigate_to_homepage()
    product_cards = home_page.get_all_product_cards()
    for card in product_cards:
        card.click()
        home_page.expect_page_to_have_url(f"{home_page.base_url}/")
