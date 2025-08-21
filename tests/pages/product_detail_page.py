from .base_page import BasePage
from ..locators import product_detail_page_locators
from ..locators import homepage_locators
import time
import random
import requests


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

    def click_menu_item(self, menu_name):
        menu_items = {
            "products": homepage_locators.PRODUCTS_MENU_ITEM,
            "cart": homepage_locators.CART_MENU_ITEM,
            "login": homepage_locators.LOGIN_MENU_ITEM,
            "register": homepage_locators.REGISTER_MENU_ITEM,
        }
        key = str(menu_name).lower()
        if key in menu_items:
            self.click_element(menu_items[key])

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
        self.expect_element_to_be_visible(
            product_detail_page_locators.PRODUCT_DESCRIPTION
        )

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
        self.expect_element_to_be_visible(
            product_detail_page_locators.ADD_TO_CART_BUTTON
        )

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
        quantity_input = self.get_element(product_detail_page_locators.QUANTITY_INPUT)
        start_value = int(quantity_input.get_attribute("value"))
        quantity_input.press("ArrowUp")
        time.sleep(1)
        return start_value + 1

    def sum_all_prices_in_cart(self):
        all_prices = self.get_elements(product_detail_page_locators.ALL_PRICES_IN_CART)
        total_price = 0
        for price in all_prices:
            total_price += float(price.text_content().replace("$", ""))
        return total_price

    def delete_all_products_from_cart(self):
        while True:
            buttons = self.get_elements(
                product_detail_page_locators.REMOVE_FROM_CART_BUTTON
            )
            if not buttons:
                break
            buttons[0].click()
            self.page.wait_for_timeout(1000)

    def clear_all_comments(self):
        """Clear all comments using the admin endpoint"""

        # Login as admin using JWT endpoint (NOT session-based login)
        session = requests.Session()
        login_response = session.post(
            "https://web-production-c47e.up.railway.app/api/auth/token/",  # JWT endpoint
            json={"username": "Admin", "password": "Admin"},
        )

        if login_response.status_code != 200:
            raise Exception(f"Login failed with status {login_response.status_code}")

        # Get JWT token from response
        token_data = login_response.json()
        token = token_data.get("access")  # JWT returns 'access' token
        if not token:
            raise Exception(f"No access token received. Response: {token_data}")

        print(f"Login successful, token: {token[:20]}...")

        # Set up headers with JWT token
        headers = {"Authorization": f"Bearer {token}"}

        try:
            # Use the new clear_all endpoint
            clear_response = session.delete(
                "https://web-production-c47e.up.railway.app/api/comments/clear_all/",
                headers=headers,
            )

            if clear_response.status_code == 204:
                print("✅ All comments cleared successfully!")
                return True
            else:
                print(f"❌ Failed to clear comments: {clear_response.status_code}")
                print(f"Response: {clear_response.text}")
                return False

        except Exception as e:
            print(f"Error in clear_all_comments: {e}")
            return False
