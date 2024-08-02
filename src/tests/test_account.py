import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("init_driver")
class TestAccount(BaseTest):

    def test_update_account_details(self, config):
        self.driver.get(config["base_url"])
        login_page = LoginPage(self.driver)
        login_page.enter_username(config["login"]["username"])
        login_page.enter_password(config["login"]["password"])
        login_page.click_sign_in_button()

        account_page = AccountPage(self.driver)
        # Perform actions to update account details
        # Add assertions to verify account updates
