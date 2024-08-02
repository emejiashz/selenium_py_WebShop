from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".s-main-slot .s-result-item")

    def click_first_product(self):
        self.wait_for_element(*self.FIRST_PRODUCT).click()
