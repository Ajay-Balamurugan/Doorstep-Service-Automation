import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class EmployeeRegistrationPage(BasePage):
    NAME_FIELD = (By.ID, "user_name")
    EMAIL_FIELD = (By.ID, "user_email")
    PASSWORD_FIELD = (By.ID, "user_password")
    PASSWORD_CONFIRMATION_FIELD = (By.ID, "user_password_confirmation")
    SKILL_DROPDOWN_FIELD = (By.ID, "user_service_id")
    CREATE_BUTTON = (By.XPATH, "//input[@type='submit']")
    ADMIN_DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")


    # select.select_by_visible_text("Option 1")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)


    def create_employee(self,name, email, password, password_confirmation):
        self.do_send_keys(self.NAME_FIELD, name)
        self.do_send_keys(self.EMAIL_FIELD, email)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        self.do_send_keys(self.PASSWORD_CONFIRMATION_FIELD, password_confirmation)
        skill_dropdown = self.get_element(self.SKILL_DROPDOWN_FIELD)
        self.do_click(self.SKILL_DROPDOWN_FIELD)
        select = Select(skill_dropdown)
        select.select_by_visible_text('Cleaning')
        self.do_click(self.CREATE_BUTTON)
        time.sleep(2)

    def go_to_admin_dashboard_page(self):
        self.get_element(self.ADMIN_DASHBOARD_LINK).click()
        time.sleep(1)






