from pages.base_page import BasePage
from pages.locators import BusketPageLocators


class Basket_Page(BasePage):
    def should_not_be_product_in_busket_text(self):
        assert self.find_text_in_element(*BusketPageLocators.EMPTY_BUSKET) == "Your basket is empty. Continue shopping", \
            "busket is not empty"

    def should_not_be_product_in_busket(self):
        assert self.is_not_element_present(*BusketPageLocators.PRODUCT_IN_BUSKET), \
            "There is product in busket"