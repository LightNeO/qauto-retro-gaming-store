import os
import pytest
from playwright.sync_api import sync_playwright


class TestConfig:
    """Test configuration settings

    SIMPLE USAGE - ADD 'set' BEFORE LAUNCHING PYTEST:
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
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
    SLOW_MO = int(os.getenv("SLOW_MO", "1000"))


@pytest.fixture(scope="session")
def browser_context_args():
    """Browser context arguments for each test session"""
    return {
        "ignore_https_errors": True,
        "accept_downloads": True,
    }


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch arguments for each test session"""
    return {
        "headless": TestConfig.HEADLESS,
        "slow_mo": TestConfig.SLOW_MO,
        # args for stability and CI/CD
        "args": [
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-accelerated-2d-canvas",
            "--no-first-run",
            "--no-zygote",
            "--disable-gpu",
        ],
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


@pytest.fixture
def base_url():
    """Base URL for the application"""
    return TestConfig.BASE_URL
