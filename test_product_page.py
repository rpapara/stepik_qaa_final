from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

test_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, test_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(str(time.time()) + "@fakemail.org", "wryi12345")
        login_page.should_be_authorized_user() 
        print("setup done")
    
    def test_user_cant_see_success_message(self, browser):   
        page = ProductPage(browser, test_link)
        page.open()    
        page.should_not_be_success_message()    

    @pytest.mark.need_review 
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, test_link)
        page.open()
        page.add_product_to_basket()
        
        page.success_message_should_contain_product_title()
        page.info_message_should_contain_product_price()

links = ("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
         )
@pytest.mark.parametrize("link", links)
@pytest.mark.need_review 
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    
    page.success_message_should_contain_product_title()
    page.info_message_should_contain_product_price()
    

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason='known issue with formatting')),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    
    page.success_message_should_contain_product_title()
    page.info_message_should_contain_product_price()

def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()

def test_guest_cant_see_success_message(browser):   
    page = ProductPage(browser, test_link)
    page.open()    
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="negative test for not showing success message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()    
    
@pytest.mark.xfail(reason="negative test for disappeared success message")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_disappear()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() 

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()                    # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() 
 
@pytest.mark.need_review     
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_have_empty_basket_message()
    
def test_guest_can_see_basket_is_not_empty_after_adding_product_to_basket(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_to_basket()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_empty_basket()
    basket_page.should_not_have_empty_basket_message()