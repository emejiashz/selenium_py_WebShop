from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    def add_to_cart(self):
        self.wait_for_element(*self.ADD_TO_CART_BUTTON).click()
