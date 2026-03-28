from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class ProductPageLocators():   
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERTS = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    INFO_ALERTS = (By.CSS_SELECTOR, "div.alert-info div.alertinner strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "article.product_page h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page div.product_main p.price_color")

class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner .basket-title")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

