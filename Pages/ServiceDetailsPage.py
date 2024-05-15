import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class ServiceDetailsPage(BasePage):
    BOOK_NOW_BUTTON = (By.XPATH,"//button[text()='Book Now'][1]")
    ADD_TO_CART_BUTTON = (By.XPATH,"//button[text()='Book Now'][1]/../../following-sibling::div//input[@type='submit']")
    DATE_TIME_FIELD = (By.XPATH,"//button[text()='Book Now'][1]/../../following-sibling::div//input[@id='time_slot']")
    CART_PAGE_LINK = (By.XPATH,"//a[text()='Cart']")
    HOME_PAGE_LINK = (By.XPATH,"//a[text()='Home']")



    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)


    def add_to_cart(self):
        self.do_click(self.BOOK_NOW_BUTTON)
        # self.do_send_keys(self.DATE_TIME_FIELD,"31/05/2024, 17:50")
        self.do_send_keys(self.DATE_TIME_FIELD, "31/05/2024")
        self.do_send_keys(self.DATE_TIME_FIELD, Keys.TAB)
        self.do_send_keys(self.DATE_TIME_FIELD, "17:50")
        time.sleep(2)
        self.do_click(self.ADD_TO_CART_BUTTON)

    def go_to_cart_page(self):
        self.do_click(self.CART_PAGE_LINK)

    def go_to_home_page(self):
        self.do_click(self.HOME_PAGE_LINK)









