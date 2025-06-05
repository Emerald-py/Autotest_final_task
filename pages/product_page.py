from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocator.BUTTON_BASKET), "Add to basket button is missing"

    def add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE).text
        button_basket = self.browser.find_element(*ProductPageLocator.BUTTON_BASKET)
        button_basket.click()
        self.solve_quiz_and_get_code()
        name_after_adding = self.browser.find_element(*ProductPageLocator.NAME_AFTER_ADDING).text
        price_after_adding = self.browser.find_element(*ProductPageLocator.PRICE_AFTER_ADDING).text
        assert product_name == name_after_adding, "The wrong item has been added to basket"
        assert product_price == price_after_adding, "Incorrect price of the added product"
