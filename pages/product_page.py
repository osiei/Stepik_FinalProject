from .locators import BusketPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
        def add_product(self):
            login_link = self.browser.find_element(*BusketPageLocators.ADD_BUTTON)
            login_link.click()
        def check_name_product_in_busket(self):
            assert self.find_text_in_element(*BusketPageLocators.NAME_PRODUCT) == self.find_text_in_element(*BusketPageLocators.ALERT_NAME_PRODUCT_IN_BUSKET), "Name product not in busket"
        def check_sum_product_in_busket(self):
            assert self.find_text_in_element(*BusketPageLocators.SUM_PRODUCT) == self.find_text_in_element(*BusketPageLocators.ALERT_SUM_PRODUCT_IN_BUSKET), "Wrong sum product in busket"