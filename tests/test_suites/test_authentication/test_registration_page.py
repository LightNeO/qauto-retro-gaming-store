import pytest
from tests.test_data import registration_page_test_data
from tests.locators import registration_page_locators
from tests.utils.timer_helper import TimerHelper
from playwright.sync_api import expect


@pytest.mark.test
def test_registration_page_loads_within_10_seconds(registration_page):
    """
    TC-001: Verify registration page loads within 10 seconds
    """
    timer = TimerHelper()
    timer.start()

    registration_page.navigate_to_registration_page()
    registration_page.wait_for_page_load()
    registration_page.wait_for_main_content()
    title = registration_page.get_element_text(registration_page_locators.REGISTRATION_PAGE_TITLE)
    load_time_ms = timer.stop()

    assert load_time_ms <= registration_page_test_data.PERFORMANCE_THRESHOLD_MS, (
        f"Registration page took {load_time_ms:.2f}ms to load, "
        f"expected - {registration_page_test_data.PERFORMANCE_THRESHOLD_MS}ms"
    )

    assert title == registration_page_test_data.EXPECTED_REGISTRATION_PAGE_TITLE, (
        f"Registration page title is '{title}', expected - '{registration_page_test_data.EXPECTED_REGISTRATION_PAGE_TITLE}'"
    )
