from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGES_TITLE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    MESSAGES_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    BOOK_TITLE = (By.TAG_NAME, "h1")
    BOOK_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")                                  

class BasketPageLocators():
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    GOODS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET = (By.XPATH, '//*[@id="content_inner"]/p')
