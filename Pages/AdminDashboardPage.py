import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class AdminDashboardPage(BasePage):
    MANAGE_SERVICES_LINK = (By.XPATH, "//a[text()='Manage Services']")
    DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")
    ACCEPT_BUTTON = (By.XPATH, "//table[@id='customer_bookings_table']/tbody/tr[1]/td/a")
    EMPLOYEE_SELECT_DROPDOWN = (By.XPATH, "//select[@id='employee_slot_user_id']")
    ASSIGN_EMPLOYEE_BUTTON = (By.XPATH, "//input[@value = 'Assign Employee']")



    # select.select_by_visible_text("Option 1")


    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)


    def go_to_services_page(self):
        self.get_element(self.MANAGE_SERVICES_LINK).click()
        time.sleep(1)

    def assign_employee(self):
        self.do_click(self.ACCEPT_BUTTON)
        employee_dropdown = self.get_element(self.EMPLOYEE_SELECT_DROPDOWN)
        self.do_click(self.EMPLOYEE_SELECT_DROPDOWN)
        select = Select(employee_dropdown)
        select.select_by_index(1)
        self.do_click(self.ASSIGN_EMPLOYEE_BUTTON)
        time.sleep(3)





