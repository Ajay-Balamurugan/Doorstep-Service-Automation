import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Login')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_on_login_link(self):
        self.do_click(self.LOGIN_LINK)




