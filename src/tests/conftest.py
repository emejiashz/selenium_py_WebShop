import json
import pathlib

import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request, config):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        web_driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        web_driver = webdriver.Firefox(options=options)

    else:
        pytest.fail("Unsupported browser!")
    web_driver.get(config["env_url"])
    web_driver.maximize_window()

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="session")
def config():
    """Load configuration from a JSON file."""
    config_path = pathlib.Path('../config/config.json')
    if not config_path.is_file():
        pytest.fail(f"Config file not found: {config_path}")
    try:
        with open(config_path) as config_file:
            data = json.load(config_file)
    except json.JSONDecodeError as e:
        pytest.fail(f"Error parsing JSON from config file: {e}")
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")
    return data
