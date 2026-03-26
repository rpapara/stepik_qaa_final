from .pages.product_page import ProductPage
import pytest


links = ("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
         )

@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    
    page.success_message_must_contain_product_title()
    page.info_message_must_contain_product_price()
    




    