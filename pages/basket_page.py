from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Item is presented in basket"

    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE),  \
            'The basket is empty message is not presented'