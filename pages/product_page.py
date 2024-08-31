from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from re import search

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_message_item_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ITEM), "Message Item-in-cart is not presented"

    def should_be_correct_text_in_message_item_in_cart(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        message_item = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM)
        assert search(item_name.text, message_item.text), "Item-name not found in Message Item-in-cart"

    def should_be_message_price_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), "Message Price-cart is not presented"

    def should_be_correct_amount_in_message_price_cart(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        assert search(item_price.text, message_price.text), "Item-price not found in Message Price-cart"

