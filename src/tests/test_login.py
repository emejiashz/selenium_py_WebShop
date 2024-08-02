import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.home_page import HomePage


@pytest.mark.usefixtures("init_driver")
class TestLogin(BaseTest):

    def test_login(self, config):
        self.driver.get(config["base_url"])
        login_page = LoginPage(self.driver)
        login_page.enter_username(config["login"]["username"])
        login_page.enter_password(config["login"]["password"])
        login_page.click_sign_in_button()
        # Add assertions to verify successful login
