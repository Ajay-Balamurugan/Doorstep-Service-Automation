import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class AdminDashboardPage(BasePage):
    MANAGE_SERVICES_LINK = (By.XPATH, "//a[text()='Manage Services']")
    DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")
    ACCEPT_BUTTON = (By.XPATH, "//table[@id='customer_bookings_table']/tbody/tr[1]/td/a")
    # ACCEPT_BUTTON = (By.XPATH, "//table[@id='customer_bookings_table']/tbody/td[text() = 'Cleaning']/a")
    ACCEPT_CLEANING_BUTTON = (By.XPATH, "//td[contains(text() ,'Cleaning')]/..//a")
    EMPLOYEE_SELECT_DROPDOWN = (By.XPATH, "//select[@id='employee_slot_user_id']")
    ASSIGN_EMPLOYEE_BUTTON = (By.XPATH, "//input[@value = 'Assign Employee']")
    CREATE_ADMIN_LINK = (By.XPATH, "//a[text()='Create Admin']")
    CREATE_EMPLOYEE_LINK = (By.XPATH, "//a[text()='Create Employee']")
    LOG_OUT_BUTTON = (By.XPATH, "//button[text()='Log Out']")



    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    def go_to_services_page(self):
        self.get_element(self.MANAGE_SERVICES_LINK).click()
        time.sleep(1)

    def accept_service(self):
        self.do_click(self.ACCEPT_BUTTON)
        time.sleep(2)
        return self.current_url()



    def assign_employee(self, name=""):
        self.do_click(self.EMPLOYEE_SELECT_DROPDOWN)
        employee_dropdown = self.get_element(self.EMPLOYEE_SELECT_DROPDOWN)
        select = Select(employee_dropdown)
        if name == "":
            select.select_by_index(0)
        else:
            select.select_by_visible_text(name)
        self.do_click(self.ASSIGN_EMPLOYEE_BUTTON)
        time.sleep(3)

    def go_to_admin_create_page(self):
        self.do_click(self.CREATE_ADMIN_LINK)

    def go_to_employee_create_page(self):
        self.do_click(self.CREATE_EMPLOYEE_LINK)

    def do_log_out(self):
        self.do_click(self.LOG_OUT_BUTTON)

    def accept_cleaning_service(self):
        self.do_click(self.ACCEPT_CLEANING_BUTTON)








