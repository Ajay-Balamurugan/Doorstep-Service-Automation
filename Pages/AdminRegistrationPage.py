import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class AdminRegistrationPage(BasePage):
    NAME_FIELD = (By.ID, "user_name")
    EMAIL_FIELD = (By.ID, "user_email")
    PASSWORD_FIELD = (By.ID, "user_password")
    PASSWORD_CONFIRMATION_FIELD = (By.ID, "user_password_confirmation")

    CREATE_BUTTON = (By.XPATH, "//input[@type='submit']")

    # select.select_by_visible_text("Option 1")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)


    def create_admin(self,name, email, password, password_confirmation):
        self.do_send_keys(self.NAME_FIELD, name)
        self.do_send_keys(self.EMAIL_FIELD, email)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        self.do_send_keys(self.PASSWORD_CONFIRMATION_FIELD, password_confirmation)
        self.do_click(self.CREATE_BUTTON)
        time.sleep(2)

    def assign_employee(self):
        self.do_click(self.ACCEPT_BUTTON)
        employee_dropdown = self.get_element(self.EMPLOYEE_SELECT_DROPDOWN)
        self.do_click(self.EMPLOYEE_SELECT_DROPDOWN)
        select = Select(employee_dropdown)
        select.select_by_index(1)
        self.do_click(self.ASSIGN_EMPLOYEE_BUTTON)
        time.sleep(3)

    def go_to_admin_create_page(self):
        self.do_click(self.CREATE_ADMIN_LINK)

    def go_to_employee_create_page(self):
        self.do_click(self.CREATE_EMPLOYEE_LINK)






