from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class RegistrationFormLocators():
    EMAIL_TEXT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_TEXT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_TEXT_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class BusketPageLocators():
    BUSKET_BUTTON = (
    By.CSS_SELECTOR, ".btn-group > a")
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    SUM_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    ALERT_NAME_PRODUCT_IN_BUSKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ALERT_SUM_PRODUCT_IN_BUSKET = (
        By.CSS_SELECTOR,
        ".alert.alert-safe.alert-noicon.alert-info.fade.in >.alertinner > p:nth-child(1) > strong")
    EMPTY_BUSKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_IN_BUSKET = (By.CSS_SELECTOR, "#basket_formset > div > div")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
