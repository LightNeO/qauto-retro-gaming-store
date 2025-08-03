from tests.pages.base_page import BasePage
from tests.locators import homepage_locators


class HomePage(BasePage):

    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def navigate_to_homepage(self):
        self.page.goto(self.base_url)
        self.wait_for_page_load()

    def get_all_product_images(self):
        product_containers = self.page.locator(
            f"{homepage_locators.PRODUCTS_SECTION} > div"
        )
        product_images = []

        for i in range(product_containers.count()):
            product_container = product_containers.nth(i)
            product_image = product_container.locator("div > img")
            product_images.append(product_image)

        return product_images

    def get_all_product_cards(self):
        return self.get_elements(f"{homepage_locators.PRODUCTS_SECTION} > div")

    def get_all_view_details_buttons(self):
        return self.get_elements(homepage_locators.ALL_VIEW_DETAILS_BUTTONS)

    def get_menu_items(self):
        return [
            (homepage_locators.PRODUCTS_MENU_ITEM, "Products"),
            (homepage_locators.CART_MENU_ITEM, "Cart"),
            (homepage_locators.LOGIN_MENU_ITEM, "Login"),
            (homepage_locators.REGISTER_MENU_ITEM, "Register"),
        ]

    def get_footer_quick_links(self):
        return homepage_locators.FOOTER_QUICK_LINKS

    def get_social_media_links(self):
        return homepage_locators.SOCIAL_MEDIA_LINKS

    def click_menu_item(self, menu_name):
        menu_items = {
            "products": homepage_locators.PRODUCTS_MENU_ITEM,
            "cart": homepage_locators.CART_MENU_ITEM,
            "login": homepage_locators.LOGIN_MENU_ITEM,
            "register": homepage_locators.REGISTER_MENU_ITEM,
        }
        if menu_name.lower() in menu_items:
            self.click_element(menu_items[menu_name.lower()])

    def click_product_card(self, index=0):
        product_cards = self.get_all_product_cards()
        if index < len(product_cards):
            product_cards[index].click()

    def click_view_details_button(self, index=0):
        buttons = self.get_all_view_details_buttons()
        if index < len(buttons):
            buttons[index].click()

    def hover_menu_item(self, menu_name):
        menu_items = {
            "products": homepage_locators.PRODUCTS_MENU_ITEM,
            "cart": homepage_locators.CART_MENU_ITEM,
            "login": homepage_locators.LOGIN_MENU_ITEM,
            "register": homepage_locators.REGISTER_MENU_ITEM,
        }
        if menu_name.lower() in menu_items:
            self.hover_element_by_locator(menu_items[menu_name.lower()])

    def hover_view_details_button(self, index=0):
        buttons = self.get_all_view_details_buttons()
        if index < len(buttons):
            self.hover_element_by_element(buttons[index])

    def move_mouse_away(self):
        self.page.mouse.move(0, 0)

    def get_header_text(self):
        return self.get_element_text(homepage_locators.HEADER)

    def get_footer_sections_text(self):
        return self.get_element_text(homepage_locators.FOOTER)

    def get_product_count(self):
        products = self.get_elements(f"{homepage_locators.PRODUCTS_SECTION} > div")
        return len(products)

    def verify_product_image_loaded(self, product_index=0):
        product_images = self.get_all_product_images()
        if product_index < len(product_images):
            image = product_images[product_index]
            width = image.evaluate("el => el.naturalWidth")
            height = image.evaluate("el => el.naturalHeight")
            return width > 0 and height > 0
        return False

    def verify_user_logged_in(self):
        return self.is_element_visible(
            homepage_locators.PROFILE_MENU_ITEM
        ) and self.is_element_visible(homepage_locators.LOGOUT_MENU_ITEM)

    def verify_user_logged_out(self):
        return self.is_element_visible(
            homepage_locators.LOGIN_MENU_ITEM
        ) and self.is_element_visible(homepage_locators.REGISTER_MENU_ITEM)

    def logout(self):
        if self.is_element_visible(homepage_locators.LOGOUT_MENU_ITEM):
            self.click_element(homepage_locators.LOGOUT_MENU_ITEM)

    def expect_page_title(self, expected_title):
        self.expect_page_to_have_title(expected_title)

    def expect_footer_visible(self):
        self.expect_element_to_be_visible(homepage_locators.FOOTER)

    def expect_social_media_icons_visible(self):
        for icon in self.get_social_media_links():
            self.expect_element_to_be_visible(icon)
