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
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")



class BusketPageLocators():
    BUSKET_BUTTON=(By.CSS_SELECTOR,"#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    SUM_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    ALERT_NAME_PRODUCT_IN_BUSKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ALERT_SUM_PRODUCT_IN_BUSKET = (
    By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    EMPTY_BUSKET = (By.CSS_SELECTOR,"#content_inner > p")
    PRODUCT_IN_BUSKET = (By.CSS_SELECTOR, "#basket_formset > div > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
