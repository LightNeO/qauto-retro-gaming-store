
class BasePage:

    def __init__(self, page):
        self.page = page

    def wait_for_element(self, locator, timeout=10000):
        try:
            self.page.wait_for_selector(locator, timeout=timeout)
        except Exception as e:
            raise Exception(f"Element {locator} not found within {timeout}ms: {e}")

    def click_element(self, locator):
        try:
            self.page.click(locator)
        except Exception as e:
            raise Exception(f"Failed to click element {locator}: {e}")

    def fill_element(self, locator, text):
        try:
            self.page.fill(locator, text)
        except Exception as e:
            raise Exception(f"Failed to fill element {locator} with '{text}': {e}")

    def get_element_text(self, locator):
        try:
            return self.page.locator(locator).text_content()
        except Exception as e:
            raise Exception(f"Failed to get text from element {locator}: {e}")

    def is_element_visible(self, locator):
        try:
            return self.page.is_visible(locator)
        except Exception:
            return False

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")
