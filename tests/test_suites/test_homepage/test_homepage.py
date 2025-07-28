import pytest
from tests.test_data import homepage_test_data
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
