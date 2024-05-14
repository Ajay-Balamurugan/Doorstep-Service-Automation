import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Login')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def lick_on_login_button(self):
        time.sleep(1)
        self.do_click(self.LOGIN_BUTTON)




