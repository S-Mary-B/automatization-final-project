from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPageLocators():
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".breadcrumb .active")
    MESSAGE_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    HEADER_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
