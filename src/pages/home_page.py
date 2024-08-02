from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def enter_search_term(self, term):
        self.wait_for_element(*self.SEARCH_BOX).send_keys(term)

    def click_search_button(self):
        self.wait_for_element(*self.SEARCH_BUTTON).click()
