import pytest
import time
from tests.test_data import registration_page_test_data
from tests.locators import registration_page_locators, login_page_locators
from tests.utils.timer_helper import TimerHelper
from playwright.sync_api import expect


@pytest.mark.smoke
def test_registration_page_loads_within_10_seconds(registration_page):
    """
    TC-001: Verify registration page loads within 10 seconds
    """
    timer = TimerHelper()
    timer.start()

    registration_page.navigate_to_registration_page()
    registration_page.wait_for_page_load()
    load_time_ms = timer.stop()

    assert load_time_ms <= registration_page_test_data.PERFORMANCE_THRESHOLD_MS, (
        f"Registration page took {load_time_ms:.2f}ms to load, "
        f"expected - {registration_page_test_data.PERFORMANCE_THRESHOLD_MS}ms"
    )


@pytest.mark.smoke
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


@pytest.mark.smoke
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


@pytest.mark.smoke
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


@pytest.mark.smoke
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


@pytest.mark.smoke
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


@pytest.mark.smoke
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


@pytest.mark.smoke
def test_username_is_required(registration_page):
    """
    TC-022: Verify username is required

    Steps:
    1. Navigate to registration page
    2. Enter valid email
    3. Enter valid password
    4. Click register button
    5. Verify that the username field is invalid
    """
    registration_page.navigate_to_registration_page()
    registration_page.get_element(registration_page_locators.EMAIL_FIELD).fill(
        registration_page_test_data.get_random_email()
    )
    registration_page.get_element(registration_page_locators.PASSWORD_FIELD).fill(
        registration_page_test_data.get_random_password()
    )
    registration_page.get_element(registration_page_locators.REGISTER_BUTTON).click()
    username_field = registration_page.get_element(registration_page_locators.USERNAME_FIELD)
    is_valid = username_field.evaluate("el => el.checkValidity()")
    assert not is_valid


@pytest.mark.smoke
def test_email_is_required(registration_page):
    """
    TC-023: Verify email is required

    Steps:
    1. Navigate to registration page
    2. Enter valid username
    3. Enter valid password
    4. Click register button
    5. Verify that the email field is invalid
    """
    registration_page.navigate_to_registration_page()
    registration_page.get_element(registration_page_locators.USERNAME_FIELD).fill(
        registration_page_test_data.get_random_username()
    )
    registration_page.get_element(registration_page_locators.PASSWORD_FIELD).fill(
        registration_page_test_data.get_random_password()
    )
    registration_page.get_element(registration_page_locators.REGISTER_BUTTON).click()
    email_field = registration_page.get_element(registration_page_locators.EMAIL_FIELD)
    is_valid = email_field.evaluate("el => el.checkValidity()")
    assert not is_valid


@pytest.mark.smoke
def test_password_is_required(registration_page):
    """
    TC-024: Verify password is required

    Steps:
    1. Navigate to registration page
    2. Enter valid username
    3. Enter valid email
    4. Click register button
    5. Verify that the password field is invalid
    """
    registration_page.navigate_to_registration_page()
    registration_page.get_element(registration_page_locators.USERNAME_FIELD).fill(
        registration_page_test_data.get_random_username()
    )
    registration_page.get_element(registration_page_locators.EMAIL_FIELD).fill(
        registration_page_test_data.get_random_email()
    )
    registration_page.get_element(registration_page_locators.REGISTER_BUTTON).click()
    password_field = registration_page.get_element(registration_page_locators.PASSWORD_FIELD)
    is_valid = password_field.evaluate("el => el.checkValidity()")
    assert not is_valid


@pytest.mark.smoke
def test_registration_with_existing_username(registration_page):
    """
    TC-025: Verify registration with existing username

    Steps:
    1. Navigate to registration page
    2. Enter existing username
    3. Enter valid email
    4. Enter valid password
    5. Click register button
    6. Verify that the registration is not successful
    """
    registration_page.navigate_to_registration_page()
    registration_page.get_element(registration_page_locators.USERNAME_FIELD).fill(
        registration_page_test_data.EXISTING_USERNAME
    )
    registration_page.get_element(registration_page_locators.EMAIL_FIELD).fill(
        registration_page_test_data.get_random_email()
    )
    registration_page.get_element(registration_page_locators.PASSWORD_FIELD).fill(
        registration_page_test_data.get_random_password()
    )
    registration_page.get_element(registration_page_locators.REGISTER_BUTTON).click()
    actual_error = registration_page.get_element(registration_page_locators.REGISTRATION_MESSAGE)
    expected_error = registration_page_test_data.EXPECTED_REGISTRATION_ERROR_MESSAGE
    expect(actual_error).to_contain_text(expected_error)


@pytest.mark.fail_expected
def test_registration_with_existing_email(registration_page):
    """
    TC-026: Verify registration with existing email

    Steps:
    1. Navigate to registration page
    2. Enter valid username
    3. Enter existing email
    4. Enter valid password
    5. Click register button
    6. Verify that the registration is not successful
    """
    registration_page.navigate_to_registration_page()
    registration_page.get_element(registration_page_locators.USERNAME_FIELD).fill(
        registration_page_test_data.get_random_username()
    )
    registration_page.get_element(registration_page_locators.EMAIL_FIELD).fill(
        registration_page_test_data.EXISTING_EMAIL
    )
    registration_page.get_element(registration_page_locators.PASSWORD_FIELD).fill(
        registration_page_test_data.get_random_password()
    )
    registration_page.get_element(registration_page_locators.REGISTER_BUTTON).click()
    actual_error = registration_page.get_element(registration_page_locators.REGISTRATION_MESSAGE)
    expected_error = registration_page_test_data.EXPECTED_REGISTRATION_ERROR_MESSAGE_EMAIL
    try:
        expect(actual_error).to_contain_text(expected_error)
    except AssertionError:
        pytest.fail("THIS FAIL IS EXPECTED")


@pytest.mark.smoke
def test_registration_with_valid_data(registration_page):
    """
    TC-027: Verify registration with valid data and redirection to login page

    Steps:
    1. Navigate to registration page
    2. Enter valid username
    3. Enter valid email
    4. Enter valid password
    5. Click register button
    6. Verify that the registration is successful
    7. Verify that the user is redirected to login page
    """
    registration_page.navigate_to_registration_page()
    registration_page.get_element(registration_page_locators.USERNAME_FIELD).fill(
        registration_page_test_data.get_random_username()
    )
    registration_page.get_element(registration_page_locators.EMAIL_FIELD).fill(
        registration_page_test_data.get_random_email()
    )
    registration_page.get_element(registration_page_locators.PASSWORD_FIELD).fill(
        registration_page_test_data.get_random_password()
    )
    registration_page.get_element(registration_page_locators.REGISTER_BUTTON).click()
    actual_message = registration_page.get_element(registration_page_locators.REGISTRATION_MESSAGE)
    expected_message = registration_page_test_data.EXPECTED_REGISTRATION_SUCCESS_MESSAGE
    expect(actual_message).to_contain_text(expected_message)
    time.sleep(1)
    registration_page.wait_for_page_load()
    login_page_title = registration_page.get_element_text(login_page_locators.TITLE)
    assert login_page_title == "Login"


@pytest.mark.test
def test_registration_with_email_without_at_sign(registration_page):
    """
    TC-028: Verify registration with email without @ sign

    Steps:
    1. Navigate to registration page
    2. Enter valid username
    3. Enter invalid email
    4. Enter valid password
    5. Click register button
    6. Verify that the registration is not successful
    """
    registration_page.navigate_to_registration_page()
    username_field = registration_page.get_element(registration_page_locators.USERNAME_FIELD)
    username_field.fill(
        registration_page_test_data.get_random_username()
    )
    email_field = registration_page.get_element(registration_page_locators.EMAIL_FIELD)
    email_field.fill(
        registration_page_test_data.get_email_without_at()
    )
    password_field = registration_page.get_element(registration_page_locators.PASSWORD_FIELD)
    password_field.fill(
        registration_page_test_data.get_random_password()
    )
    register_button = registration_page.get_element(registration_page_locators.REGISTER_BUTTON)
    register_button.click()
    email_field = registration_page.get_element(registration_page_locators.EMAIL_FIELD)
    is_valid = email_field.evaluate("el => el.checkValidity()")
    assert not is_valid


@pytest.mark.fail_expected
def test_registration_with_email_without_dot(registration_page):
    """
    TC-029: Verify registration with email without dot

    Steps:
    1. Navigate to registration page
    2. Enter valid username
    3. Enter email without dot
    4. Enter valid password
    5. Click register button
    6. Verify that the registration is not successful
    """
    registration_page.navigate_to_registration_page()
    username_field = registration_page.get_element(registration_page_locators.USERNAME_FIELD)
    username_field.fill(
        registration_page_test_data.get_random_username()
    )
    email_field = registration_page.get_element(registration_page_locators.EMAIL_FIELD)
    email_field.fill(
        registration_page_test_data.get_email_without_dot()
    )
    password_field = registration_page.get_element(registration_page_locators.PASSWORD_FIELD)
    password_field.fill(
        registration_page_test_data.get_random_password()
    )
    register_button = registration_page.get_element(registration_page_locators.REGISTER_BUTTON)
    register_button.click()
    email_field = registration_page.get_element(registration_page_locators.EMAIL_FIELD)
    is_valid = email_field.evaluate("el => el.checkValidity()")
    try:
        assert not is_valid
    except AssertionError:
        pytest.fail("THIS FAIL IS EXPECTED")


@pytest.mark.test
def test_registration_with_email_without_domain(registration_page):
    """
    TC-030: Verify registration with email without domain

    Steps:
    1. Navigate to registration page
    2. Enter valid username
    3. Enter email without domain
    4. Enter valid password
    5. Click register button
    6. Verify that the registration is not successful
    """
    registration_page.navigate_to_registration_page()
    username_field = registration_page.get_element(registration_page_locators.USERNAME_FIELD)
    username_field.fill(
        registration_page_test_data.get_random_username()
    )
    email_field = registration_page.get_element(registration_page_locators.EMAIL_FIELD)
    email_field.fill(
        registration_page_test_data.get_email_without_domain()
    )
    password_field = registration_page.get_element(registration_page_locators.PASSWORD_FIELD)
    password_field.fill(
        registration_page_test_data.get_random_password()
    )
    register_button = registration_page.get_element(registration_page_locators.REGISTER_BUTTON)
    register_button.click()
    email_field = registration_page.get_element(registration_page_locators.EMAIL_FIELD)
    is_valid = email_field.evaluate("el => el.checkValidity()")
    assert not is_valid
