import time

import pytest
from Config.config import TestData
from Pages.ServiceDetailsPage import ServiceDetailsPage
from Pages.CartPage import CartPage
from Pages.BookingHistoryPage import BookingHistoryPage
from Database.ServiceRequestItems import ServiceRequestItemsDB
from Database.ServiceRequests import ServiceRequestsDB


from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_CustomerScenario(BaseTest):
    def test_scenario(self):

        """PAGES"""
        time.sleep(2)
        self.HomePage = HomePage(self.driver)
        self.ServiceDetailsPage = ServiceDetailsPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.CartPage = CartPage(self.driver)
        self.BookingHistoryPage = BookingHistoryPage(self.driver)

        """DATABASE"""
        service_request_items_table = ServiceRequestItemsDB()
        service_requests_table = ServiceRequestsDB()

        """AUTOMATION"""
        self.HomePage.click_on_login_link()

        self.loginPage.do_login(TestData.CUSTOMER_EMAIL, TestData.CUSTOMER_PASSWORD)

        self.HomePage.go_to_cleaning_page()
        old_cart_items_count = service_request_items_table.get_service_request_items_count()
        self.ServiceDetailsPage.add_to_cart()
        self.ServiceDetailsPage.go_to_home_page()

        self.HomePage.go_to_plumbing_page()
        self.ServiceDetailsPage.add_to_cart()
        new_cart_items_count = service_request_items_table.get_service_request_items_count()
        assert new_cart_items_count == old_cart_items_count + 2
        self.ServiceDetailsPage.go_to_cart_page()

        self.CartPage.remove_first_item_from_cart()
        old_orders_count = service_requests_table.get_service_requests_count()
        self.CartPage.place_order()
        new_orders_count = service_requests_table.get_service_requests_count()
        assert new_orders_count == old_orders_count + 1

        time.sleep(2)
        self.CartPage.go_to_booking_history_page()

        self.BookingHistoryPage.view_booking_details()

        time.sleep(5)



