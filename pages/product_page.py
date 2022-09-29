from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def should_be_products_name_in_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_added = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text
        assert product_added == product_name, 'The names in cart do not match'

    def should_be_products_price_in_cart(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price_of_added_product = self.browser.find_element(*ProductPageLocators.PRICE_ADDED).text
        assert product_price == price_of_added_product, 'The prices in cart do not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_success_message_dissaper(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message has not disappeared'




