import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class CartPage(BasePage):
    PLACE_ORDER_BUTTON = (By.ID, "place_order_btn")
    REMOVE_FROM_CART_BUTTON = (By.XPATH, "//button[text() = 'Remove'][1]")
    BOOKING_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'Booking History')]")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)



    def remove_first_item_from_cart(self):
        self.do_click(self.REMOVE_FROM_CART_BUTTON)
        time.sleep(2)

    def place_order(self):
        self.do_click(self.PLACE_ORDER_BUTTON)
        time.sleep(2)

    def go_to_booking_history_page(self):
        self.do_click(self.BOOKING_HISTORY_LINK)


