import pytest
from playwright.sync_api import expect
from tests.test_data import homepage_test_data
from tests.locators import homepage_locators
from tests.utils.timer_helper import TimerHelper


@pytest.mark.atomic
@pytest.mark.smoke
def test_homepage_loads_within_5_seconds(page, base_url):
    """
    TC-001: Verify homepage loads within 8 seconds

    Steps:
    1. Start timer
    2. Navigate to homepage
    3. Wait for page to load (main content visible)
    4. Stop timer
    5. Verify load time is within 8 seconds
    """
    # Step 1: Start timer
    timer = TimerHelper()
    timer.start()

    # Step 2: Navigate to homepage
    page.goto(base_url)

    # Step 3: Wait for page to load (main content visible)
    page.wait_for_selector(homepage_locators.MAIN_CONTENT, timeout=10000)

    # Step 4: Stop timer
    load_time_ms = timer.stop()

    # Step 5: Verify load time is within 8 seconds (use assert for numbers)
    assert load_time_ms <= homepage_test_data.PERFORMANCE_THRESHOLD_MS, (
        f"Homepage took {load_time_ms:.2f}ms to load, "
        f"expected - {homepage_test_data.PERFORMANCE_THRESHOLD_MS}ms"
    )

    # Additional verification: Check page title (use expect for web elements)
    expect(page).to_have_title(homepage_test_data.EXPECTED_HOMEPAGE_TITLE)
