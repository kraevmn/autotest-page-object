import time
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def product_add(self):
        product_add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON)
        product_add_button.click()

    def check_product_title(self):
        messages1 = self.browser.find_element(*ProductPageLocators.MESSAGES_TITLE)
        messages2 = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        assert messages1.text == messages2.text, "Названия книги и название в корзине отличаются"

    def check_product_price(self):
        messages3 = self.browser.find_element(*ProductPageLocators.MESSAGES_PRICE)
        messages4 = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert messages3.text == messages4.text, "Цена книги и цена в корзине отличаются"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"