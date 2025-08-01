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
    load_time_ms = timer.stop()

    assert load_time_ms <= registration_page_test_data.PERFORMANCE_THRESHOLD_MS, (
        f"Registration page took {load_time_ms:.2f}ms to load, "
        f"expected - {registration_page_test_data.PERFORMANCE_THRESHOLD_MS}ms"
    )


@pytest.mark.test
def test_registration_page_has_correct_title(registration_page):
    """
    TC-017: Verify registration page has correct title

    Steps:
    1. Navigate to registration page
    2. Verify page has correct title
    """
    registration_page.navigate_to_registration_page()
    title = registration_page.get_element_text(
        registration_page_locators.REGISTRATION_PAGE_TITLE
    )
    assert (
        title == registration_page_test_data.EXPECTED_REGISTRATION_PAGE_TITLE
    ), f"Registration page title is '{title}', expected - '{registration_page_test_data.EXPECTED_REGISTRATION_PAGE_TITLE}'"


@pytest.mark.test
def test_username_field_is_present(registration_page):
    """
    TC-018: Verify username field is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify username field is present
    """
    registration_page.navigate_to_registration_page()

    expect(
        registration_page.get_element(registration_page_locators.USERNAME_FIELD)
    ).to_be_visible()


@pytest.mark.test
def test_email_field_is_present(registration_page):
    """
    TC-019: Verify email field is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify email field is present
    """
    registration_page.navigate_to_registration_page()

    expect(
        registration_page.get_element(registration_page_locators.EMAIL_FIELD)
    ).to_be_visible()


@pytest.mark.test
def test_password_field_is_present(registration_page):
    """
    TC-019: Verify password field is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify password field is present
    """
    registration_page.navigate_to_registration_page()

    expect(
        registration_page.get_element(registration_page_locators.PASSWORD_FIELD)
    ).to_be_visible()


@pytest.mark.test
def test_register_button_is_present(registration_page):
    """
    TC-021: Verify register button is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify register button is present
    """
    registration_page.navigate_to_registration_page()

    expect(
        registration_page.get_element(registration_page_locators.REGISTER_BUTTON)
    ).to_be_visible()


@pytest.mark.test
def test_already_have_an_account_link_is_present(registration_page):
    """
    TC-022: Verify already have an account link is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify already have an account link is present
    """
    registration_page.navigate_to_registration_page()

    expect(
        registration_page.get_element(
            registration_page_locators.ALREADY_HAVE_AN_ACCOUNT_LINK
        )
    ).to_be_visible()
