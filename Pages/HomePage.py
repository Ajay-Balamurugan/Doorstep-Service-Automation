import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Login')]")
    SERVICE_LINK_CLEANING = (By.XPATH, "//p[text()='Cleaning']/preceding-sibling::a")
    SERVICE_LINK_PEST_CONTROL = (By.XPATH,"//p[text()='Pest Control']/preceding-sibling::a")
    BOOK_NOW_BUTTON = (By.XPATH, "//button[text()='Book Now'][1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_on_login_link(self):
        self.do_click(self.LOGIN_LINK)

    def go_to_cleaning_page(self):
        self.do_click(self.SERVICE_LINK_CLEANING)

    def go_to_pest_control_page(self):
        self.do_click(self.SERVICE_LINK_PEST_CONTROL)







