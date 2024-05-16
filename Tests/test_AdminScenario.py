import time

import pytest
from Config.config import TestData
from Database.services import ServicesDB
from Database.ServiceRequestItems import ServiceRequestItemsDB
from Pages.AdminDashboardPage import AdminDashboardPage
from Pages.HomePage import HomePage
from Pages.OptionManagementPage import OptionManagementPage
from Pages.ServiceManagementPage import ServiceManagementPage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_AdminScenario(BaseTest):
    def get_id(self, url: str):
        return int(url.split("/")[-1])
    def test_scenario(self):

        """PAGES"""
        self.HomePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.AdminDashboardPage = AdminDashboardPage(self.driver)
        self.ServiceManagementPage = ServiceManagementPage(self.driver)
        self.OptionManagementPage = OptionManagementPage(self.driver)

        """DATABASE"""
        services_table = ServicesDB()
        service_request_items_table = ServiceRequestItemsDB()



        """AUTOMATION"""
        time.sleep(2)
        self.HomePage.click_on_login_link()

        self.loginPage.do_login(TestData.ADMIN_EMAIL, TestData.ADMIN_PASSWORD)

        self.AdminDashboardPage.go_to_services_page()

        old_services_count = services_table.get_services_total_count()
        self.ServiceManagementPage.create_service("test_service", "test_description", "/Users/abalamurugan/PycharmProjects/DoorStepServiceAutomation/Images/image1.jpg")
        new_services_count = services_table.get_services_total_count()
        assert new_services_count == old_services_count + 1

        option_url = self.ServiceManagementPage.go_to_options_page()
        option_id = self.get_id(option_url)

        old_options_count = services_table.options_count_for_service(option_id)
        self.OptionManagementPage.create_option("test_option_1", "option_1_description",  2, 800)
        self.OptionManagementPage.create_option("test_option_2", "option_2_description",  3, 1000)
        self.OptionManagementPage.update_option("updated_option_title", "updated_option_description", 3, 200)
        new_options_count = services_table.options_count_for_service(option_id)
        assert new_options_count == old_options_count + 2
        time.sleep(2)

        self.OptionManagementPage.go_to_admin_dashboard_page()

        service_request_item_url = self.AdminDashboardPage.accept_service()
        service_request_item_id = self.get_id(service_request_item_url)
        old_status = service_request_items_table.get_service_request_item_status(service_request_item_id)
        self.AdminDashboardPage.assign_employee()
        new_status = service_request_items_table.get_service_request_item_status(service_request_item_id)
        assert old_status != new_status
        time.sleep(3)


