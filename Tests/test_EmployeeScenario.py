import time

import pytest
from Config.config import TestData
from Pages.AdminDashboardPage import AdminDashboardPage
from Pages.AdminRegistrationPage import AdminRegistrationPage
from Pages.EmployeeRegistrationPage import EmployeeRegistrationPage

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_EmployeeScenario(BaseTest):
    def test_scenario(self):
        time.sleep(2)
        self.HomePage = HomePage(self.driver)
        self.HomePage.click_on_login_link()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.ADMIN_EMAIL, TestData.ADMIN_PASSWORD)

        self.AdminDashboardPage = AdminDashboardPage(self.driver)
        self.AdminDashboardPage.go_to_admin_create_page()

        self.AdminRegistrationPage = AdminRegistrationPage(self.driver)
        self.AdminRegistrationPage.create_admin(TestData.NEW_ADMIN_NAME,TestData.NEW_ADMIN_EMAIL,TestData.NEW_ADMIN_PASSWORD,TestData.NEW_ADMIN_PASSWORD)

        self.AdminDashboardPage.do_log_out()
        self.HomePage.click_on_login_link()
        self.loginPage.do_login(TestData.NEW_ADMIN_EMAIL, TestData.NEW_ADMIN_PASSWORD)

        self.AdminDashboardPage.go_to_employee_create_page()

        self.EmployeeRegistrationPage = EmployeeRegistrationPage(self.driver)
        self.EmployeeRegistrationPage.create_employee(TestData.EMPLOYEE_NAME,TestData.EMPLOYEE_EMAIL,TestData.EMPLOYEE_PASSWORD,TestData.EMPLOYEE_PASSWORD)
        self.EmployeeRegistrationPage.go_to_admin_dashboard_page()

        self.AdminDashboardPage.accept_cleaning_service()
        self.AdminDashboardPage.assign_employee(TestData.EMPLOYEE_NAME)
        time.sleep(1)

        self.AdminDashboardPage.do_log_out()

        self.HomePage.click_on_login_link()
        self.loginPage.do_login(TestData.EMPLOYEE_EMAIL,TestData.EMPLOYEE_PASSWORD)
        time.sleep(3)


