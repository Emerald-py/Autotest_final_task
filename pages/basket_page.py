from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty but should be empty"

    def no_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There are items in the basket, but they shouldn't be there"
