from .base_page import BasePage
from ..locators import product_detail_page_locators
from ..locators import homepage_locators
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

    # Quantity and cart methods
    def set_quantity(self, quantity):
        """Set product quantity"""
        pass

    def increase_quantity(self):
        """Increase quantity by 1"""
        pass

    def decrease_quantity(self):
        """Decrease quantity by 1"""
        pass

    def get_current_quantity(self):
        """Get current quantity value"""
        pass

    def click_add_to_cart(self):
        """Click add to cart button"""
        pass

    # Product specifications methods
    def get_product_specifications(self):
        """Get product specifications text"""
        pass

    # Related products methods
    def get_related_products(self):
        """Get list of related products"""
        pass

    def click_related_product(self, index):
        """Click on related product by index"""
        pass

    # Reviews methods
    def get_product_reviews(self):
        """Get all product reviews"""
        pass

    def get_review_count(self):
        """Get total number of reviews"""
        pass

    def get_review_author(self, review_index):
        """Get review author by review index"""
        pass

    def get_review_date(self, review_index):
        """Get review date by review index"""
        pass

    def get_review_text(self, review_index):
        """Get review text by review index"""
        pass

    def get_review_rating(self, review_index):
        """Get review rating by review index"""
        pass

    # Validation methods
    def is_product_detail_page_loaded(self):
        """Check if product detail page is loaded"""
        pass

    def is_add_to_cart_button_present(self):
        """Check if add to cart button is present"""
        pass

    def is_product_image_displayed(self):
        """Check if product image is displayed"""
        pass

    def is_quantity_selector_present(self):
        """Check if quantity selector is present"""
        pass

    def is_product_gallery_present(self):
        """Check if product gallery is present"""
        pass

    def is_reviews_section_present(self):
        """Check if reviews section is present"""
        pass

    def is_related_products_present(self):
        """Check if related products section is present"""
        pass
