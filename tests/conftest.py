import os
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import APIRequestContext
from tests.pages.home_page import HomePage
from tests.pages.registration_page import RegistrationPage
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.product_detail_page import ProductDetailPage
from tests.utils.logger import logger
from tests.utils.api_auth import APIAuth


class TestConfig:
    """Test configuration settings

    SIMPLE USAGE - ADD 'set' BEFORE LAUNCHING PYTEST:

    PowerShell:
    set BROWSER=firefox
    python -m pytest tests/

    CMD:
    set BROWSER=firefox
    python -m pytest tests/

    EXAMPLES:
    set BROWSER=firefox          # Use Firefox browser
    set BROWSER=chromium         # Use Chrome browser
    set BROWSER=webkit           # Use Safari browser
    set HEADLESS=false           # Show browser window
    set SLOW_MO=2000             # Add 2 second delays
    set BASE_URL=http://localhost:3000  # Test local environment
    """

    BASE_URL = os.getenv("BASE_URL", "https://web-production-c47e.up.railway.app")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", "20000"))
    SLOW_MO = int(os.getenv("SLOW_MO", "1000"))
    API_LOGIN_PATHS = os.getenv("API_LOGIN_PATHS", "").split(",") if os.getenv("API_LOGIN_PATHS") else None


@pytest.fixture(scope="session")
def browser_context_args():
    """Browser context arguments for each test session"""
    return {
        "ignore_https_errors": True,
        "accept_downloads": True,
        "no_viewport": True,  # Fullscreen mode
    }


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch arguments for each test session"""
    return {
        "headless": TestConfig.HEADLESS,
        "slow_mo": TestConfig.SLOW_MO,
        "args": ["--start-maximized"],  # Fullscreen mode
    }


@pytest.fixture(scope="session")
def playwright():
    """Playwright instance for the test session"""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright, browser_type_launch_args):
    """Browser instance for the test session"""
    if TestConfig.BROWSER == "chromium":
        browser = playwright.chromium.launch(**browser_type_launch_args)
    elif TestConfig.BROWSER == "firefox":
        browser = playwright.firefox.launch(**browser_type_launch_args)
    elif TestConfig.BROWSER == "webkit":
        browser = playwright.webkit.launch(**browser_type_launch_args)
    else:
        browser = playwright.chromium.launch(**browser_type_launch_args)

    yield browser
    browser.close()


@pytest.fixture
def context(browser, browser_context_args):
    """Browser context for each test"""
    context = browser.new_context(**browser_context_args)
    yield context
    context.close()


@pytest.fixture
def page(context):
    """Page instance for each test"""
    page = context.new_page()
    page.set_default_timeout(TestConfig.TIMEOUT)
    yield page
    page.close()


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application"""
    return TestConfig.BASE_URL


@pytest.fixture(scope="session")
def api_request_context(playwright, base_url) -> APIRequestContext:
    return playwright.request.new_context(base_url=base_url, ignore_https_errors=True)


@pytest.fixture(scope="session")
def api_auth(base_url):
    return APIAuth(base_url=base_url, login_paths=TestConfig.API_LOGIN_PATHS)


@pytest.fixture(scope="session")
def storage_state_logged_in(api_request_context, api_auth):
    username = os.getenv("API_USERNAME", "testuser123")
    password = os.getenv("API_PASSWORD", "Test@123")
    storage_state = api_auth.login_and_build_storage_state(
        api_request_context=api_request_context,
        username=username,
        password=password,
    )
    return storage_state


@pytest.fixture
def context_logged_in(browser, browser_context_args, storage_state_logged_in):
    args = dict(browser_context_args)
    args.update({"storage_state": storage_state_logged_in})
    ctx = browser.new_context(**args)
    yield ctx
    ctx.close()


@pytest.fixture
def page_logged_in(context_logged_in):
    pg = context_logged_in.new_page()
    pg.set_default_timeout(TestConfig.TIMEOUT)
    yield pg
    pg.close()


@pytest.fixture
def home_page(page, base_url):
    """HomePage instance for each homepagetest"""
    return HomePage(page, base_url)


@pytest.fixture
def home_page_logged_in(page_logged_in, base_url):
    return HomePage(page_logged_in, base_url)


@pytest.fixture
def registration_page(page, base_url):
    """RegistrationPage instance for each registration page test"""
    return RegistrationPage(page, base_url + "/register")


@pytest.fixture
def login_page(page, base_url):
    """LoginPage instance for each login page test"""
    return LoginPage(page, base_url + "/login")


@pytest.fixture
def products_page(page, base_url):
    """ProductsPage instance for each products page test"""
    return ProductsPage(page, base_url + "/products")


@pytest.fixture
def product_detail_page(page, base_url):
    """ProductDetailPage instance for each product detail page test"""
    return ProductDetailPage(page, base_url)


@pytest.fixture
def products_page_logged_in(page_logged_in, base_url):
    return ProductsPage(page_logged_in, base_url + "/products")


@pytest.fixture
def product_detail_page_logged_in(page_logged_in, base_url):
    return ProductDetailPage(page_logged_in, base_url)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture test result and log failures.
    This hook is executed for each test function.
    """
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # We only look at the final result of the test (when 'call' is happening)
    if report.when == "call":
        if report.failed:
            # Get the test name and the failure details
            test_name = item.name
            error_message = report.longreprtext
            logger.error(f"Test Failed: {test_name}")
            logger.error(f"Failure Details:\n{error_message}")
        elif report.passed:
            logger.info(f"Test Passed: {item.name}")
        elif report.skipped:
            logger.warning(f"Test Skipped: {item.name}")
