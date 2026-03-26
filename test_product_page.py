from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    
    page.success_message_must_contain_product_title()
    page.info_message_must_contain_product_price()
    




    