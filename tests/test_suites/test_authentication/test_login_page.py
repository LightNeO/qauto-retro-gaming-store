import pytest
from tests.test_data import login_page_test_data
from tests.utils.performance_helper import PerformanceHelper


@pytest.mark.smoke
def test_login_page_loads_within_10_seconds(login_page):
    """
    TC-031: Verify login page loads within 10 seconds
    """
    PerformanceHelper.assert_page_loads_within_threshold(
        login_page, 
        login_page.navigate_to_login_page, 
        login_page_test_data.PERFORMANCE_THRESHOLD_MS, 
        "Login page"
    )


@pytest.mark.smoke
def test_login_page_has_correct_title(login_page):
    """
    TC-032: Verify login page has correct title
    """
    login_page.navigate_to_login_page()
    login_page.expect_title_to_have_text("Login")


@pytest.mark.smoke
def test_username_field_is_present(login_page):
    """
    TC-033: Verify username field is present on login page
    """
    login_page.navigate_to_login_page()
    login_page.expect_username_field_to_be_visible()


@pytest.mark.smoke
def test_password_field_is_present(login_page):
    """
    TC-034: Verify password field is present on login page
    """
    login_page.navigate_to_login_page()
    login_page.expect_password_field_to_be_visible()


@pytest.mark.smoke
def test_login_button_is_present(login_page):
    """
    TC-035: Verify login button is present on login page
    """
    login_page.navigate_to_login_page()
    login_page.expect_login_button_to_be_visible()


@pytest.mark.smoke
def test_username_field_is_required(login_page):
    """
    TC-036: Verify username field is required

    Steps:
    1. Navigate to login page
    2. Enter valid password
    3. Click on login button
    4. Verify that the username field is invalid
    """
    login_page.navigate_to_login_page()
    login_page.login_with_empty_username(login_page_test_data.get_random_password())
    assert not login_page.is_username_field_valid()


@pytest.mark.smoke
def test_password_is_required(login_page):
    """
    TC-037: Verify password field is required

    Steps:
    1. Navigate to login page
    2. Enter valid username
    3. Click on login button
    4. Verify that the password field is invalid
    """
    login_page.navigate_to_login_page()
    login_page.login_with_empty_password(login_page_test_data.get_random_username())
    assert not login_page.is_password_field_valid()


@pytest.mark.smoke
def test_error_message_is_displayed_for_invalid_login(login_page):
    """
    TC-038: Verify error message is displayed for invalid login

    Steps:
    1. Navigate to login page
    2. Enter invalid username
    3. Enter invalid password
    4. Click on login button
    5. Verify that the error message is displayed
    """
    login_page.navigate_to_login_page()
    login_page.login_with_invalid_data()
    login_page.expect_login_message_to_have_text(login_page_test_data.EXPECTED_ERROR_MESSAGE)


@pytest.mark.smoke
def test_use_remains_on_login_page_after_invalid_login(login_page):
    """
    TC-039: Verify user remains on login page after invalid login

    Steps:
    1. Navigate to login page
    2. Enter invalid username
    3. Enter invalid password
    4. Click on login button
    5. Verify that the user remains on login page
    """
    login_page.navigate_to_login_page()
    login_page.login_with_invalid_data()
    login_page.expect_title_to_have_text(login_page_test_data.EXPECTED_TITLE)


@pytest.mark.smoke
def test_field_are_not_cleared_after_invalid_login(login_page):
    """
    TC-040: Verify form fields are not cleared after invalid login

    Steps:
    1. Navigate to login page
    2. Enter invalid username
    3. Enter invalid password
    4. Click on login button
        5. Verify that the form fields are not cleared
    """
    login_page.navigate_to_login_page()
    login_page.login_with_invalid_data()
    login_page.expect_username_field_to_have_value(login_page_test_data.INVALID_USERNAME)
    login_page.expect_password_field_to_have_value(login_page_test_data.INVALID_PASSWORD)


@pytest.mark.smoke
def test_succes_message_is_displayed_for_valid_login(login_page):
    """
    TC-040: Verify successful message is displayed after valid login

    Steps:
    1. Navigate to login page
    2. Enter existing username
    3. Enter valid password
    4. Click on login button
    5. Verify that the successful message is displayed
    """
    login_page.navigate_to_login_page()
    login_page.login_with_existing_user()
    login_page.expect_login_message_to_have_text(login_page_test_data.EXPECTED_SUCCESS_MESSAGE)


@pytest.mark.smoke
def test_user_is_redirected_to_homepage_after_successful_login(login_page):
    """
    TC-042: Verify user is redirected to homepage after successful login

    Steps:
    1. Navigate to login page
    2. Enter existing username
    3. Enter valid password
    4. Click on login button
    5. Verify that the user is redirected to homepage
    6. Verify that the user is logged in
    """
    login_page.navigate_to_login_page()
    login_page.login_with_existing_user()
    login_page.wait_for_page_load()
    assert login_page.verify_user_logged_in()


@pytest.mark.smoke
def test_jwt_token_is_stored_after_successful_login(login_page):
    """
    TC-043: Verify JWT token is stored after successful login

    Steps:
    1. Navigate to login page
    2. Enter existing username
    3. Enter valid password
    4. Click on login button
    5. Verify that the JWT token is stored in the browser
    """
    login_page.navigate_to_login_page()
    login_page.login_with_existing_user()
    login_page.wait_for_page_load()

    assert login_page.verify_jwt_token_stored(), "JWT token not found in browser localStorage"


@pytest.mark.smoke
def test_logout_proccess_completes_successfully(login_page):
    """
    TC-044: Verify logout proccess completes successfully

    Steps:
    1. Navigate to login page
    2. Enter existing username
    3. Enter valid password
    4. Click on login button
    5. Click on logout button
    7. Verify that the user is logged out
    """
    login_page.navigate_to_login_page()
    login_page.login_with_existing_user()
    login_page.wait_for_page_load()
    login_page.logout()
    login_page.wait_for_page_load()
    assert login_page.verify_user_logged_out()


@pytest.mark.smoke
def test_jwt_token_is_cleared_after_logout(login_page):
    """
    TC-045: Verify JWT token is cleared after logout

    Steps:
    1. Navigate to login page
    2. Enter existing username
    3. Enter valid password
    4. Click on login button
    5. Click on logout button
    6. Verify that the JWT token is cleared from the browser
    """
    login_page.navigate_to_login_page()
    login_page.login_with_existing_user()
    login_page.wait_for_page_load()
    login_page.logout()
    login_page.wait_for_page_load()
    assert login_page.verify_jwt_token_cleared(), "JWT token not cleared from browser"
