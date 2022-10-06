from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '//*[@class="btn-group"]/*[@class="btn btn-default"]')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_ADDED = (By.CSS_SELECTOR, '.alertinner>strong')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    PRICE_ADDED =(By.CSS_SELECTOR, '.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(2)')

class BasketPageLocators():
    ITEM_IN_BASKET = (By.CSS_SELECTOR,'.basket-items')
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR,'#content_inner')




