import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("init_driver")
class TestSearch(BaseTest):
    def test_search(self, config):
        self.driver.get(config["base_url"])
        home_page = HomePage(self.driver)
        home_page.enter_search_term("laptop")
        home_page.click_search_button()
        search_results_page = SearchResultsPage(self.driver)
        search_results_page.click_first_product()
        # Add assertions to verify search results