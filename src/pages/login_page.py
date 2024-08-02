from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "ap_email")
    PASSWORD_INPUT = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")

    def enter_username(self, username):
        self.wait_for_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_sign_in_button(self):
        self.wait_for_element(*self.SIGN_IN_BUTTON).click()
