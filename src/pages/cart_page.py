from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    DELETE_BUTTON = (By.CSS_SELECTOR, ".sc-action-delete input")

    def delete_first_item(self):
        self.wait_for_element(*self.DELETE_BUTTON).click()
