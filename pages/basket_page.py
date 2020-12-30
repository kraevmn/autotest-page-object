from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS), "Goods in basket, but should not be"

    def should_be_empty_basket_text(self):
        messages1 = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
        messages1 = messages1.text
#        print(f"Text: {messages1}")
        assert messages1 == 'Ваша корзина пуста Продолжить покупки', "Ваша корзина не пуста!"
