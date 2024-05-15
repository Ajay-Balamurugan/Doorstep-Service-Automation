import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class BookingHistoryPage(BasePage):
    VIEW_DETAILS_LINK = (By.XPATH, "(//a[text()='View Details'])[last()]")


    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)


    def view_booking_details(self):
        self.do_click(self.VIEW_DETAILS_LINK)


