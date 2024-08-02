import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    driver: WebDriver = None
