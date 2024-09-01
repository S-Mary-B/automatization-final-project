import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import time

@pytest.mark.parametrize('promo_link', ["?promo=offer0",
                                        "?promo=offer1",
                                        "?promo=offer2",
                                        "?promo=offer3",
                                        "?promo=offer4",
                                        "?promo=offer5",
                                        "?promo=offer6",
                                        pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                        "?promo=offer8",
                                        "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_message_item_in_cart()
    page.should_be_correct_text_in_message_item_in_cart()
    page.should_be_message_price_cart()
    page.should_be_correct_amount_in_message_price_cart()

