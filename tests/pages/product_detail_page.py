from .base_page import BasePage
from ..locators import product_detail_page_locators
from ..locators import homepage_locators
import time
import random


class ProductDetailPage(BasePage):
    """
    Product Detail Page Object Model
    Contains methods for interacting with product detail page elements
    """

    def __init__(self, page, base_url):
        super().__init__(page)
        self.page = page
        self.base_url = base_url

    # Navigation methods
    def navigate_to_product_detail_by_id(self, product_id):
        self.page.goto(f"{self.base_url}/product/?id={product_id}")

    def navigate_to_random_product_detail_page(self):
        self.navigate_to_product_detail_by_id(random.randrange(1, 10))

    def back_to_products(self):
        self.page.click(homepage_locators.PRODUCTS_MENU_ITEM)
        pass

    # Product information methods
    def get_product_name(self):
        return self.get_element_text(product_detail_page_locators.PRODUCT_NAME)

    def expect_product_name_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.PRODUCT_NAME)

    def get_product_price_without_currency(self):
        return self.get_element_text(
            product_detail_page_locators.PRODUCT_PRICE
        ).replace("$", "")

    def expect_product_price_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.PRODUCT_PRICE)

    def get_product_description(self):
        return self.get_element_text(product_detail_page_locators.PRODUCT_DESCRIPTION)

    def expect_product_description_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.PRODUCT_DESCRIPTION)

    def get_avarage_rating(self):
        return self.get_element_text(product_detail_page_locators.AVARAGE_RATING)

    def expect_avarage_rating_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.AVARAGE_RATING)

    def get_rating_count(self):
        return self.get_element_text(product_detail_page_locators.RATING_COUNT)

    def expect_rating_count_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.RATING_COUNT)

    def get_rating_stars(self):
        return self.get_element_text(product_detail_page_locators.RATING_STARS)

    def expect_rating_stars_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.RATING_STARS)

    def get_product_image_src(self):
        return self.get_element_attribute(
            product_detail_page_locators.PRODUCT_IMAGE, "src"
        )

    def get_add_to_cart_button(self):
        return self.get_element(product_detail_page_locators.ADD_TO_CART_BUTTON)

    def expect_add_to_cart_button_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.ADD_TO_CART_BUTTON)

    def get_quantity_input(self):
        return self.get_element(product_detail_page_locators.QUANTITY_INPUT)

    def expect_quantity_input_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.QUANTITY_INPUT)

    def get_comment_input(self):
        return self.get_element(product_detail_page_locators.COMMENT_INPUT)

    def expect_comment_input_to_be_visible(self):
        self.expect_element_to_be_visible(product_detail_page_locators.COMMENT_INPUT)

    def get_product_image(self):
        return self.get_element(product_detail_page_locators.PRODUCT_IMAGE)

    def expect_product_image_to_be_visible(self):
        product_image = self.get_product_image()
        image_width = product_image.evaluate("el => el.naturalWidth")
        image_height = product_image.evaluate("el => el.naturalHeight")
        assert (
            image_width > 0 and image_height > 0
        ), "Product image failed to load(EXPECTED FOR IMAGE ID 10)"

    def click_add_to_cart_button(self):
        self.click_element(product_detail_page_locators.ADD_TO_CART_BUTTON)

    def check_error_message_after_click(self, element_locator):
        dialog_message = None

        def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            dialog.accept()
        self.page.on("dialog", handle_dialog)
        self.click_element(element_locator)
        self.page.wait_for_timeout(1000)
        return dialog_message

    def increase_quantity_and_return_new_value(self):
        quantity_input = self.get_element(
            product_detail_page_locators.QUANTITY_INPUT
        )
        start_value = int(quantity_input.get_attribute("value"))
        quantity_input.press("ArrowUp")
        time.sleep(1)
        return start_value + 1

