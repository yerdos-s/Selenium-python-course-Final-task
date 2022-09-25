from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, 'There is no login in url'

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert True, 'Login form is not presented'

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert True, 'Register form is not presented'
