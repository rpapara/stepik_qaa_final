from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERTS), \
        "Success message is not presented, but should be"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERTS), \
        "Success message is presented, but should not be"
    
    def success_message_should_contain_product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        success_messages = self.browser.find_elements(*ProductPageLocators.SUCCESS_ALERTS)
        
        product_title_found = False
        for i in range(len(success_messages)):
            message = success_messages[i]
            if product_title == message.text:   
                print(f"Product title: {product_title} found in success message number {i+1}: {message.text}")
                product_title_found = True
                break               
        
        assert product_title_found, f"Product title not found in success messages. Should be: {product_title}, but presented: {[message.text for message in success_messages]}"
    
    def info_message_should_contain_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        info_messages = self.browser.find_elements(*ProductPageLocators.INFO_ALERTS)
        
        product_price_found = False
        
        for i in range(len(info_messages)):
            message = info_messages[i]
            if product_price == message.text:
                print(f"Product price: {product_price} found in info message number {i+1}: {message.text}")
                product_price_found = True
                break   
        
        assert product_price_found, f"Product price not found in info messages. Should be: {product_price}, but presented: {[message.text for message in info_messages]}"
        
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERTS), \
        "Success message is presented, but should be disappeared"