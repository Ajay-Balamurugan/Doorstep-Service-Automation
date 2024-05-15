import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Login')]")
    CLEANING_SERVICE_LINK = (By.XPATH, "//p[text()='Cleaning']/preceding-sibling::a")
    PLUMBING_SERVICE_LINK = (By.XPATH,"//p[text()='Plumbing']/preceding-sibling::a")
    BOOK_NOW_BUTTON = (By.XPATH, "//button[text()='Book Now'][1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_on_login_link(self):
        self.do_click(self.LOGIN_LINK)

    def go_to_cleaning_page(self):
        self.do_click(self.CLEANING_SERVICE_LINK)

    def go_to_plumbing_page(self):
        self.do_click(self.PLUMBING_SERVICE_LINK)







