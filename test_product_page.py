import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_message_item_in_cart()
    page.should_be_correct_text_in_message_item_in_cart()
    page.should_be_message_price_cart()
    page.should_be_correct_amount_in_message_price_cart()

