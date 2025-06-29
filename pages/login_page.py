from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_ADDRESS)
        email_address.send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        user_password.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
