from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
        "Basket is not empty, but should be"
 
    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTENT), \
        "Basket is empty, but should not"
           
    def should_have_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
        "Basket empty message is not presented, but should be"
        
    def should_not_have_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
        "Basket empty message is presented, but should not"