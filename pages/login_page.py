from .base_page import BasePage
from .locators import LoginPageLocators, RegistrationFormLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL) #переход к странице регистрации
        login_link.click()
        email_text = self.browser.find_element(*RegistrationFormLocators.EMAIL_TEXT)
        email_text.send_keys(email)
        password_text=self.browser.find_element(*RegistrationFormLocators.PASSWORD_TEXT)
        password_text.send_keys(password)
        password_text_confirm = self.browser.find_element(*RegistrationFormLocators.PASSWORD_TEXT_CONFIRM)
        password_text_confirm.send_keys(password)
        reg_button = self.browser.find_element(*RegistrationFormLocators.REGISTRATION_BUTTON)  # переход к странице регистрации
        reg_button.click()




