import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("init_driver")
class TestPurchase(BaseTest):

    def test_purchase(self, config):
        self.driver.get(config["base_url"])
        login_page = LoginPage(self.driver)
        login_page.enter_username(config["login"]["username"])
        login_page.enter_password(config["login"]["password"])
        login_page.click_sign_in_button()

        home_page = HomePage(self.driver)
        home_page.enter_search_term("laptop")
        home_page.click_search_button()

        search_results_page = SearchResultsPage(self.driver)
        search_results_page.click_first_product()

        product_page = ProductPage(self.driver)
        product_page.add_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.delete_first_item()
        # Add assertions to verify purchase flow
