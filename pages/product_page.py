from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not present"

    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def book_name_is_right(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_in_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_IN_THE_BASKET)
        assert book_name.text == book_in_basket_name.text, "Name of the book does not resemble the item in the basket"

    def price_is_right(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_of_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET)
        assert book_price.text == price_of_basket.text, "Total value of basket does not equal the price of the book"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_IN_THE_BASKET), \
            "Success message is presented, but should not be"

    def element_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_IN_THE_BASKET), \
            "Element did not disappear"
