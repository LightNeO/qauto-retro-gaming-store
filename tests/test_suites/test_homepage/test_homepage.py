import pytest
from tests.test_data import homepage_test_data
from tests.locators import homepage_locators
from tests.utils.timer_helper import TimerHelper
from playwright.sync_api import expect


class TestHomepage:

    @pytest.mark.smoke
    def test_homepage_loads_within_10_seconds(self, home_page):
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
    def test_homepage_displays_correct_title(self, home_page):
        """
        TC-002: Verify homepage displays correct page title

        Steps:
        1. Navigate to homepage
        2. Verify page has correct title
        """
        home_page.navigate_to_homepage()
        expect(home_page.page).to_have_title(homepage_test_data.EXPECTED_HOMEPAGE_TITLE)

    @pytest.mark.smoke
    def test_header_contains_expected_data(self, home_page):
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
        header_text_clean = ' '.join(header_text.split())

        for expected_item in homepage_test_data.EXPECTED_HEADER_DATA:
            assert expected_item in header_text_clean, (
                f"Expected header item '{expected_item}' not found"
            )

    @pytest.mark.smoke
    def test_menu_items_hover_effects(self, home_page):
        """
        TC-007: Verify menu items hover effects

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
            (homepage_locators.REGISTER_MENU_ITEM, "Register")
        ]
        
        for locator, menu_name in menu_items:
            # Hover over menu item
            home_page.page.hover(locator)
            
            # Verify hover effect is applied
            hover_state = home_page.get_menu_hover_state(locator)
            assert hover_state, f"{menu_name} menu hover effect not applied"

    @pytest.mark.smoke
    def test_menu_items_hover_effects_disappear(self, home_page):
        """
        TC-008: Verify menu items hover effects disappear

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
            (homepage_locators.REGISTER_MENU_ITEM, "Register")
        ]
        
        for locator, menu_name in menu_items:
            # Hover over menu item
            home_page.page.hover(locator)
            
            # Move mouse away from menu item
            home_page.page.mouse.move(0, 0)
            
            # Verify hover effect disappears
            hover_state = home_page.get_menu_hover_state(locator)
            assert not hover_state, f"{menu_name} menu hover effect did not disappear"
