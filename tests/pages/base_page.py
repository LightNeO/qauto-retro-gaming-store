from playwright.sync_api import expect
from tests.utils.logger import logger


class BasePage:

    def __init__(self, page):
        self.page = page
        logger.info(f"Initialized Page: {self.__class__.__name__}")

    def wait_for_element(self, locator, timeout=10000):
        logger.info(f"Waiting for element: {locator}")
        try:
            self.page.wait_for_selector(locator, timeout=timeout)
        except Exception as e:
            logger.error(f"Element {locator} not found within {timeout}ms: {e}")
            raise

    def click_element(self, locator):
        logger.info(f"Clicking element: {locator}")
        try:
            self.page.click(locator)
        except Exception as e:
            logger.error(f"Failed to click element {locator}: {e}")
            raise

    def fill_element(self, locator, text):
        logger.info(f"Filling element {locator} with text: '{text}'")
        try:
            self.page.fill(locator, text)
        except Exception as e:
            logger.error(f"Failed to fill element {locator} with '{text}': {e}")
            raise

    def get_element_text(self, locator):
        logger.info(f"Getting text from element: {locator}")
        try:
            return self.page.locator(locator).text_content()
        except Exception as e:
            logger.error(f"Failed to get text from element {locator}: {e}")
            raise

    def is_element_visible(self, locator):
        try:
            return self.page.is_visible(locator)
        except Exception:
            return False

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    def get_elements(self, locator):
        try:
            return self.page.locator(locator).all()
        except Exception as e:
            raise Exception(f"Failed to get elements with locator {locator}: {e}")

    def get_element(self, locator):
        try:
            return self.page.locator(locator)
        except Exception as e:
            raise Exception(f"Failed to get element with locator {locator}: {e}")

    def get_attribute(self, element, attribute):
        try:
            return element.get_attribute(attribute)
        except Exception as e:
            raise Exception(f"Failed to get attribute '{attribute}' from element: {e}")

    def hover_element_by_locator(self, locator):
        try:
            self.page.hover(locator)
        except Exception as e:
            raise Exception(f"Failed to hover over element {locator}: {e}")

    def hover_element_by_element(self, element):
        try:
            element.hover()
        except Exception as e:
            raise Exception(f"Failed to hover over element: {e}")

    def get_hover_state_by_locator(self, locator):
        return self.page.locator(locator).evaluate("el => el.matches(':hover')")

    def get_hover_state_by_element(self, element):
        return element.evaluate("el => el.matches(':hover')")

    def is_field_valid(self, locator):
        return self.page.locator(locator).evaluate("el => el.checkValidity()")

    def clear_field(self, locator):
        try:
            self.page.locator(locator).fill("")
        except Exception as e:
            raise Exception(f"Failed to clear field {locator}: {e}")

    def get_field_value(self, locator):
        try:
            return self.page.locator(locator).input_value()
        except Exception as e:
            raise Exception(f"Failed to get value from field {locator}: {e}")

    def expect_element_to_be_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def expect_element_to_have_text(self, locator, text):
        expect(self.page.locator(locator)).to_have_text(text)

    def expect_element_to_contain_text(self, locator, text):
        expect(self.page.locator(locator)).to_contain_text(text)

    def expect_element_to_have_value(self, locator, value):
        expect(self.page.locator(locator)).to_have_value(value)

    def expect_page_to_have_title(self, title):
        expect(self.page).to_have_title(title)

    def expect_page_to_have_url(self, url):
        expect(self.page).to_have_url(url)

    def count_elements(self, locator):
        return self.page.locator(locator).count()

    def get_element_attribute(self, locator, attribute):
        try:
            return self.page.locator(locator).get_attribute(attribute)
        except Exception as e:
            raise Exception(f"Failed to get attribute '{attribute}' from element {locator}: {e}")
