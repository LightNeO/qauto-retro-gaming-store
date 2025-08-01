import pytest
import time
from tests.test_data import login_page_test_data
from tests.locators import login_page_locators
from tests.utils.timer_helper import TimerHelper
from playwright.sync_api import expect


@pytest.mark.smoke
def test_login_page_loads_within_10_seconds(login_page):
    """
    TC-001: Verify login page loads within 10 seconds
    """
    timer = TimerHelper()
    timer.start()

    login_page.navigate_to_login_page()
    login_page.wait_for_page_load()
    load_time_ms = timer.stop()

    assert load_time_ms <= login_page_test_data.PERFORMANCE_THRESHOLD_MS, (
        f"Login page took {load_time_ms:.2f}ms to load, "
        f"expected - {login_page_test_data.PERFORMANCE_THRESHOLD_MS}ms"
    )