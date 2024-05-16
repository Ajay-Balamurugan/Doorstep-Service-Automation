from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This is the Parent of all Pages"""

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_clear(self, by_locator):
        """Clears the text from an input field."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.clear()

    def get_element(self, by_locator):
        element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_url(self, url):
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

