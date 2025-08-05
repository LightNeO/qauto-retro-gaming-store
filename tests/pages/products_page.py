from tests.pages.base_page import BasePage
from tests.locators import products_page_locators
from tests.test_data import products_page_test_data


class ProductsPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_products_page(self):
        self.page.goto(self.base_url)
        self.wait_for_page_load()

    def expect_title_to_be_visible(self):
        self.expect_element_to_be_visible(products_page_locators.TITLE)

    def expect_title_to_have_text(self, text):
        self.expect_element_to_have_text(products_page_locators.TITLE, text)

    def get_products_grid(self):
        self.get_elements(products_page_locators.PRODUCT_CONTAINER)

    def expect_products_grid_to_be_visible(self):
        self.expect_element_to_be_visible(products_page_locators.PRODUCT_CONTAINER)

    def get_all_products_cards_amount(self):
        return self.count_elements(products_page_locators.ALL_PRODUCTS_CARDS)

    def expect_correct_amount_of_products(self, amount):
        number_of_cards = self.get_all_products_cards_amount()
        assert (
            number_of_cards == amount
        ), f"Expected {amount} products, but got {number_of_cards}"

    def get_all_product_images(self):
        return self.get_elements(products_page_locators.ALL_PRODUCTS_IMAGES)

    def expect_all_product_images_to_be_visible(self):
        all_product_images = self.get_all_product_images()
        # Use i and enumerate to get the index of the product image
        for i, product_image in enumerate(all_product_images):
            image_width = product_image.evaluate("el => el.naturalWidth")
            image_height = product_image.evaluate("el => el.naturalHeight")
            assert (
                image_width > 0 and image_height > 0
            ), f"Product {i + 1} image failed to load"

    def get_search_bar(self):
        return self.get_element(products_page_locators.SEARCH_BAR)

    def expect_search_bar_to_be_visible(self):
        self.expect_element_to_be_visible(products_page_locators.SEARCH_BAR)

    def get_search_button(self):
        return self.get_element(products_page_locators.SEARCH_BUTTON)

    def expect_search_button_to_be_visible(self):
        self.expect_element_to_be_visible(products_page_locators.SEARCH_BUTTON)

    def get_sort_dropdown(self):
        return self.get_element(products_page_locators.SORT_DROPDOWN)

    def expect_sort_dropdown_to_be_visible(self):
        self.expect_element_to_be_visible(products_page_locators.SORT_DROPDOWN)

    def search_for_product(self, product_name):
        self.get_search_bar().fill(product_name)
        self.get_search_button().click()

    def get_all_products_titles(self):
        return self.get_elements(products_page_locators.ALL_PRODUCTS_TITLES)

    def expect_no_results_message_to_be_visible(self):
        self.expect_element_to_have_text(
            products_page_locators.PRODUCT_CONTAINER,
            products_page_test_data.NO_RESULTS_TEXT,
        )

    def filter_by_low_to_high_price(self):
        self.get_sort_dropdown().select_option("Price: Low to High")

    def filter_by_high_to_low_price(self):
        self.get_sort_dropdown().select_option("Price: High to Low")

    def filter_by_top_rated(self):
        self.get_sort_dropdown().select_option("Top Rated")

    def get_all_products_prices(self):
        return self.get_elements(products_page_locators.ALL_PRODUCTS_PRICES)

    def get_all_products_ratings(self):
        return self.get_elements(products_page_locators.ALL_PRODUCTS_STAR_RATINGS)

    def expect_products_to_be_sorted_by_price_in_ascending_order(self):
        all_products_prices = self.get_all_products_prices()
        # Use i and enumerate to get the index of the product image
        for i, product_price in enumerate(all_products_prices[:-1]):
            current_price = float(product_price.text_content().replace("$", ""))
            next_price = float(all_products_prices[i + 1].text_content().replace("$", ""))
            assert (
                current_price <= next_price
            ), f"Product {i + 1} price is not in ascending order"

    def expect_products_to_be_sorted_by_price_in_descending_order(self):
        all_products_prices = self.get_all_products_prices()
        # Use i and enumerate to get the index of the product image
        for i, product_price in enumerate(all_products_prices[:-1]):
            current_price = float(product_price.text_content().replace("$", ""))
            next_price = float(all_products_prices[i + 1].text_content().replace("$", ""))
            assert (
                current_price >= next_price
            ), f"Product {i + 1} price is not in descending order"

    def expect_products_to_be_sorted_by_rating_in_descending_order(self):
        all_products_ratings = self.get_all_products_ratings()
        # Use i and enumerate to get the index of the product image
        for i, product_rating in enumerate(all_products_ratings[:-1]):
            current_rating = float(product_rating.text_content().replace("⭐ ", ""))
            next_rating = float(all_products_ratings[i + 1].text_content().replace("⭐ ", ""))
            assert (
                current_rating >= next_rating
            ), f"Product {i + 1} rating is not in descending order"
