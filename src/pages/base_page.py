"""Clase padre de las pages principales"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))

    def do_click(self, by_locator):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, self.timeout).until(EC.title_is(title))
        return self.driver.title

    def switch_window_emergent(self):
        self.driver.implicitly_wait(self.timeout)  # espera implícitamente
        self.driver.switch_to.window(self.driver.window_handles[1])

    def leng_nav(self):
        language = self.driver.execute_script("return window.navigator.language;")
        print(language)
