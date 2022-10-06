from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '//*[@class="btn-group"]/*[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_REGISTRATION = (By.CSS_SELECTOR,'input[name="registration-email"]')
    PASSWORD_REGISTRATION_1 = (By.CSS_SELECTOR,'input[name="registration-password1"]')
    PASSWORD_REGISTRATION_2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR,'[name="registration_submit"]')

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




