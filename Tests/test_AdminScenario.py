import time

import pytest
from Config.config import TestData
from Pages.AdminDashboardPage import AdminDashboardPage
from Pages.HomePage import HomePage
from Pages.OptionManagementPage import OptionManagementPage
from Pages.ServiceManagementPage import ServiceManagementPage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_AdminScenario(BaseTest):
    def test_scenario(self):
        time.sleep(2)
        self.HomePage = HomePage(self.driver)
        self.HomePage.click_on_login_link()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.ADMIN_EMAIL, TestData.ADMIN_PASSWORD)

        self.AdminDashboardPage = AdminDashboardPage(self.driver)
        self.AdminDashboardPage.go_to_services_page()

        self.ServiceManagementPage = ServiceManagementPage(self.driver)
        self.ServiceManagementPage.create_service("test_service", "test_description", "/home/ajay/PycharmProjects/Doorstep-Service-Automation/Images/image1.jpg")
        self.ServiceManagementPage.go_to_options_page()

        self.OptionManagementPage = OptionManagementPage(self.driver)
        self.OptionManagementPage.create_option("test_option_1", "option_1_description",  2, 800)
        self.OptionManagementPage.create_option("test_option_2", "option_2_description",  3, 1000)
        self.OptionManagementPage.update_option("updated_option_title", "updated_option_description", 3, 200)
        time.sleep(2)
        self.OptionManagementPage.go_to_admin_dashboard_page()

        self.AdminDashboardPage.assign_employee()

        time.sleep(3)


