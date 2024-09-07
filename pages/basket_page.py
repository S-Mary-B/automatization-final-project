from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_added_product()
        self.should_be_empty_basket_message()

    def should_not_be_added_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Product-list is presented, but should not be"
        assert True

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty-basket-message is not presented"
        assert True