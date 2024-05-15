import time

import pytest
from Config.config import TestData
from Pages.ServiceDetailsPage import ServiceDetailsPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_CustomerScenario(BaseTest):
    def test_scenario(self):
        time.sleep(2)
        self.HomePage = HomePage(self.driver)
        self.ServiceDetailsPage = ServiceDetailsPage(self.driver)
        self.loginPage = LoginPage(self.driver)


        self.HomePage.click_on_login_link()

        self.loginPage.do_login(TestData.CUSTOMER_EMAIL, TestData.CUSTOMER_PASSWORD)

        self.HomePage.go_to_cleaning_page()
        self.ServiceDetailsPage.add_to_cart()
        self.ServiceDetailsPage.go_to_home_page()

        self.HomePage.go_to_pest_control_page()
        self.ServiceDetailsPage.add_to_cart()
        self.ServiceDetailsPage.go_to_cart_page()

        time.sleep(5)



