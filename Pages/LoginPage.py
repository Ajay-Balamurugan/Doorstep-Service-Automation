import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "user_email")
    PASSWORD_FIELD = (By.ID, "user_password")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)



    def do_login(self, email, password):
        self.do_send_keys(self.EMAIL_FIELD, email)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        self.do_click(self.LOGIN_BUTTON)
        time.sleep(2)


