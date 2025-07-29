import pytest
from tests.test_data import homepage_test_data
from tests.locators import homepage_locators
from tests.utils.timer_helper import TimerHelper
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
    timer = TimerHelper()
    timer.start()

    home_page.navigate_to_homepage()
    home_page.wait_for_page_load()
    home_page.wait_for_main_content()

    load_time_ms = timer.stop()

    assert load_time_ms <= homepage_test_data.PERFORMANCE_THRESHOLD_MS, (
        f"Homepage took {load_time_ms:.2f}ms to load, "
        f"expected - {homepage_test_data.PERFORMANCE_THRESHOLD_MS}ms"
    )

    expect(home_page.page).to_have_title(homepage_test_data.EXPECTED_HOMEPAGE_TITLE)


@pytest.mark.smoke
def test_homepage_displays_correct_title(home_page):
    """
    TC-002: Verify homepage displays correct page title

    Steps:
    1. Navigate to homepage
    2. Verify page has correct title
    """
    home_page.navigate_to_homepage()
    expect(home_page.page).to_have_title(homepage_test_data.EXPECTED_HOMEPAGE_TITLE)


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
    header_text = home_page.get_element_text(homepage_locators.HEADER)
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

    # Test hover effects for all menu items
    menu_items = [
        (homepage_locators.PRODUCTS_MENU_ITEM, "Products"),
        (homepage_locators.CART_MENU_ITEM, "Cart"),
        (homepage_locators.LOGIN_MENU_ITEM, "Login"),
        (homepage_locators.REGISTER_MENU_ITEM, "Register"),
    ]

    for locator, menu_name in menu_items:
        # Hover over menu item
        home_page.page.hover(locator)

        # Verify hover effect is applied
        hover_state = home_page.get_button_hover_state(locator)
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

    # Test hover effects disappearing for all menu items
    menu_items = [
        (homepage_locators.PRODUCTS_MENU_ITEM, "Products"),
        (homepage_locators.CART_MENU_ITEM, "Cart"),
        (homepage_locators.LOGIN_MENU_ITEM, "Login"),
        (homepage_locators.REGISTER_MENU_ITEM, "Register"),
    ]

    for locator, menu_name in menu_items:
        # Hover over menu item
        home_page.page.hover(locator)

        # Move mouse away from menu item
        home_page.page.mouse.move(0, 0)

        # Verify hover effect disappears
        hover_state = home_page.get_button_hover_state(locator)
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
    expect(home_page.page.locator(homepage_locators.FOOTER)).to_be_visible()


@pytest.mark.smoke
def test_verify_footer_sections(home_page):
    """
    TC-007: Verify footer sections are visible and contain expected data

    Steps:
    1. Navigate to homepage
    2. Verify footer sections are visible and contain expected data
    """
    home_page.navigate_to_homepage()
    footer_sections = home_page.get_element_text(homepage_locators.FOOTER)
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
    footer_quick_links = homepage_locators.FOOTER_QUICK_LINKS
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
    social_media_icons = homepage_locators.SOCIAL_MEDIA_LINKS
    for icon in social_media_icons:
        expect(home_page.page.locator(icon)).to_be_visible()


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
    social_media_links = homepage_locators.SOCIAL_MEDIA_LINKS
    expected_links_text = homepage_test_data.EXPECTED_SOCIAL_MEDIA_LINKS
    failed_links = []  # collect failed links

    for link in social_media_links:
        link_text = home_page.get_element(link).get_attribute("href")
        if link_text not in expected_links_text:
            failed_links.append(f"Link '{link_text}' is broken")

    if failed_links:
        raise AssertionError(
            "Social media links validation failed:\n" + "\n".join(failed_links)
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
    home_page.wait_for_page_load()
    # Find direct child div elements of the products section
    products_in_section = home_page.page.locator(
        f"{homepage_locators.PRODUCTS_SECTION} > div"
    )
    expect(products_in_section).to_have_count(3)


@pytest.mark.test
def test_verify_all_product_images_are_visible(home_page):
    """
    TC-012: Verify all product images are visible and not broken

    Steps:
    1. Navigate to homepage
    2. Get all product images
    3. Verify each image has proper dimensions (not broken)
    """
    home_page.navigate_to_homepage()
    home_page.wait_for_page_load()
    product_images = home_page.get_all_product_images()

    # Use i and enumerate to get the index of the product image
    for i, product_image in enumerate(product_images):
        image_width = product_image.evaluate("el => el.naturalWidth")
        image_height = product_image.evaluate("el => el.naturalHeight")
        assert image_width > 0 and image_height > 0, f"Product {i + 1} image failed to load"
