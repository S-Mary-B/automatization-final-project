from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".breadcrumb .active")
    MESSAGE_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")