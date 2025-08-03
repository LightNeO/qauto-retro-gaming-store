import pytest
from tests.test_data import registration_page_test_data
from tests.utils.performance_helper import PerformanceHelper


@pytest.mark.smoke
def test_registration_page_loads_within_10_seconds(registration_page):
    """
    TC-001: Verify registration page loads within 10 seconds
    """
    PerformanceHelper.assert_page_loads_within_threshold(
        registration_page,
        registration_page.navigate_to_registration_page,
        registration_page_test_data.PERFORMANCE_THRESHOLD_MS,
        "Registration page",
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
    title = registration_page.get_page_title_text()
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
    registration_page.expect_username_field_to_be_visible()


@pytest.mark.smoke
def test_email_field_is_present(registration_page):
    """
    TC-019: Verify email field is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify email field is present
    """
    registration_page.navigate_to_registration_page()
    registration_page.expect_email_field_to_be_visible()


@pytest.mark.smoke
def test_password_field_is_present(registration_page):
    """
    TC-019: Verify password field is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify password field is present
    """
    registration_page.navigate_to_registration_page()
    registration_page.expect_password_field_to_be_visible()


@pytest.mark.smoke
def test_register_button_is_present(registration_page):
    """
    TC-021: Verify register button is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify register button is present
    """
    registration_page.navigate_to_registration_page()
    registration_page.expect_register_button_to_be_visible()


@pytest.mark.smoke
def test_already_have_an_account_link_is_present(registration_page):
    """
    TC-022: Verify already have an account link is present on registration page

    Steps:
    1. Navigate to registration page
    2. Verify already have an account link is present
    """
    registration_page.navigate_to_registration_page()
    registration_page.expect_already_have_account_link_to_be_visible()


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
    registration_page.register_with_empty_username(
        registration_page_test_data.get_random_email(),
        registration_page_test_data.get_random_password(),
    )
    assert not registration_page.is_username_field_valid()


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
    registration_page.register_with_empty_email(
        registration_page_test_data.get_random_username(),
        registration_page_test_data.get_random_password(),
    )
    assert not registration_page.is_email_field_valid()


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
    registration_page.register_with_empty_password(
        registration_page_test_data.get_random_username(),
        registration_page_test_data.get_random_email(),
    )
    assert not registration_page.is_password_field_valid()


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
    registration_page.register_with_existing_username(
        registration_page_test_data.get_random_email(),
        registration_page_test_data.get_random_password(),
    )
    registration_page.expect_registration_message_to_contain_text(
        registration_page_test_data.EXPECTED_REGISTRATION_ERROR_MESSAGE
    )


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
    registration_page.register_with_existing_email(
        registration_page_test_data.get_random_username(),
        registration_page_test_data.get_random_password(),
    )
    try:
        registration_page.expect_registration_message_to_contain_text(
            registration_page_test_data.EXPECTED_REGISTRATION_ERROR_MESSAGE_EMAIL
        )
    except AssertionError:
        pytest.fail("THIS FAIL IS EXPECTED")


@pytest.mark.test
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
    registration_page.register_with_valid_data()
    registration_page.expect_registration_message_to_contain_text(
        registration_page_test_data.EXPECTED_REGISTRATION_SUCCESS_MESSAGE
    )
    assert registration_page.verify_redirected_to_login_page()


@pytest.mark.smoke
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
    registration_page.register_with_invalid_email_format(
        registration_page_test_data.get_random_username(),
        registration_page_test_data.get_email_without_at(),
        registration_page_test_data.get_random_password(),
    )
    assert not registration_page.is_email_field_valid()


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
    registration_page.register_with_invalid_email_format(
        registration_page_test_data.get_random_username(),
        registration_page_test_data.get_email_without_dot(),
        registration_page_test_data.get_random_password(),
    )
    try:
        assert not registration_page.is_email_field_valid()
    except AssertionError:
        pytest.fail("THIS FAIL IS EXPECTED")


@pytest.mark.smoke
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
    registration_page.register_with_invalid_email_format(
        registration_page_test_data.get_random_username(),
        registration_page_test_data.get_email_without_domain(),
        registration_page_test_data.get_random_password(),
    )
    assert not registration_page.is_email_field_valid()
