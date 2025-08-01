from tests.pages.base_page import BasePage
from tests.locators import homepage_locators


class HomePage(BasePage):

    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_homepage(self):
        self.page.goto(self.base_url)

    def get_button_hover_state_by_locator(self, locator):
        return self.page.locator(locator).evaluate("el => el.matches(':hover')")

    def get_button_hover_state_by_element(self, element):
        return element.evaluate("el => el.matches(':hover')")

    def get_all_product_images(self):
        """Get all product images from the products section"""
        product_containers = self.page.locator(f"{homepage_locators.PRODUCTS_SECTION} > div")
        product_images = []
        
        for i in range(product_containers.count()):
            product_container = product_containers.nth(i)
            product_image = product_container.locator("div > img")
            product_images.append(product_image)
            
        return product_images
