import time

import pytest
from Config.config import TestData
from Pages.AdminDashboardPage import AdminDashboardPage
from Pages.AdminRegistrationPage import AdminRegistrationPage
from Pages.EmployeeRegistrationPage import EmployeeRegistrationPage
from Database.Users import UsersDB
from Database.EmployeeSlots import EmployeeSlotsDB


from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_EmployeeScenario(BaseTest):
    def test_scenario(self):
        """PAGES"""
        self.HomePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.AdminDashboardPage = AdminDashboardPage(self.driver)
        self.AdminRegistrationPage = AdminRegistrationPage(self.driver)
        self.EmployeeRegistrationPage = EmployeeRegistrationPage(self.driver)

        """DATABASE"""
        users_table = UsersDB()
        employee_slots_table = EmployeeSlotsDB()




        self.HomePage.click_on_login_link()

        self.loginPage.do_login(TestData.ADMIN_EMAIL, TestData.ADMIN_PASSWORD)

        self.AdminDashboardPage.go_to_admin_create_page()
        old_user_count = users_table.get_total_users_count()
        self.AdminRegistrationPage.create_admin(TestData.NEW_ADMIN_NAME,TestData.NEW_ADMIN_EMAIL,TestData.NEW_ADMIN_PASSWORD,TestData.NEW_ADMIN_PASSWORD)
        new_user_count = users_table.get_total_users_count()
        assert new_user_count == old_user_count + 1

        self.AdminDashboardPage.do_log_out()
        self.HomePage.click_on_login_link()
        self.loginPage.do_login(TestData.NEW_ADMIN_EMAIL, TestData.NEW_ADMIN_PASSWORD)

        self.AdminDashboardPage.go_to_employee_create_page()

        old_user_count = users_table.get_total_users_count()
        self.EmployeeRegistrationPage.create_employee(TestData.EMPLOYEE_NAME,TestData.EMPLOYEE_EMAIL,TestData.EMPLOYEE_PASSWORD,TestData.EMPLOYEE_PASSWORD)
        new_user_count = users_table.get_total_users_count()
        assert new_user_count == old_user_count + 1

        self.EmployeeRegistrationPage.go_to_admin_dashboard_page()

        self.AdminDashboardPage.accept_cleaning_service()

        old_employee_slots_count = employee_slots_table.get_employee_slots_count()
        self.AdminDashboardPage.assign_employee(TestData.EMPLOYEE_NAME)
        new_employee_slots_count = employee_slots_table.get_employee_slots_count()
        assert new_employee_slots_count == old_employee_slots_count + 1

        time.sleep(1)

        self.AdminDashboardPage.do_log_out()

        self.HomePage.click_on_login_link()
        self.loginPage.do_login(TestData.EMPLOYEE_EMAIL,TestData.EMPLOYEE_PASSWORD)
        time.sleep(3)


