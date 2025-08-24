from .base_page import BasePage
from ..locators import checkout_page_locators
from tests.test_data import checkout_page_test_data


class CheckoutPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.page = page
        self.base_url = base_url

    def navigate_to_checkout_page(self):
        self.page.goto(f"{self.base_url}/checkout")
        self.wait_for_page_load()

    def expect_checkout_page_loaded(self):
        self.expect_element_to_be_visible(checkout_page_locators.CHECKOUT_PAGE_TITLE)

    def expect_all_checkout_elements_to_be_visible(self):
        elements = [
            checkout_page_locators.PRODUCTS_CONTAINERS,
            checkout_page_locators.PRODUCTS_DESCRIPTIONS,
            checkout_page_locators.PRODUCTS_PRICES,
            checkout_page_locators.PRODUCTS_QUANTITIES,
            checkout_page_locators.PRODUCTS_SUBTOTALS,
            checkout_page_locators.TOTAL_PRICE,
            checkout_page_locators.PRODUCT_IMAGES,
            checkout_page_locators.CARD_SUMMARY,
            checkout_page_locators.FULL_NAME_FIELD,
            checkout_page_locators.EMAIL_FIELD,
            checkout_page_locators.PHONE_FIELD,
            checkout_page_locators.ADDRESS_FIELD,
            checkout_page_locators.CARD_NUMBER_FIELD,
            checkout_page_locators.CARD_EXPIRY_FIELD,
            checkout_page_locators.CARD_CVV_FIELD,
            checkout_page_locators.PLACE_ORDER_BUTTON,
        ]

        for element in elements:
            self.expect_element_to_be_visible(element)

    def fill_all_fields_with_valid_data(self):
        self.fill_element(
            checkout_page_locators.FULL_NAME_FIELD, checkout_page_test_data.VALID_NAME
        )
        self.fill_element(
            checkout_page_locators.EMAIL_FIELD, checkout_page_test_data.VALID_EMAIL
        )
        self.fill_element(
            checkout_page_locators.PHONE_FIELD, checkout_page_test_data.VALID_PHONE
        )
        self.fill_element(
            checkout_page_locators.ADDRESS_FIELD, checkout_page_test_data.VALID_ADDRESS
        )
        self.fill_element(
            checkout_page_locators.CARD_NUMBER_FIELD, checkout_page_test_data.VALID_CARD
        )
        self.fill_element(
            checkout_page_locators.CARD_EXPIRY_FIELD, checkout_page_test_data.VALID_EXPIRE_DATE
        )
        self.fill_element(
            checkout_page_locators.CARD_CVV_FIELD, checkout_page_test_data.VALID_CVV
        )

    def expect_field_to_be_valid(self, field_locator):
        return self.is_field_valid(field_locator)
