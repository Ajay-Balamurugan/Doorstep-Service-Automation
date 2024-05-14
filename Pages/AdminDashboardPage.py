import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class AdminDashboardPage(BasePage):
    MANAGE_SERVICES_LINK = (By.XPATH, "//a[text()='Manage Services']")
    CREATE_SERVICE_BUTTON = (By.ID, "create")
    TITLE_FIELD = (By.ID, "service_title")
    DESCRIPTION_FIELD = (By.ID, "service_description")
    FILE_FIELD = (By.ID, "service_images")
    SERVICE_FORM_SUBMIT_BUTTON = (By.XPATH, "//form[@id = 'create_service_form']/input[@value='Create Service']")
    DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")
    ACCEPT_BUTTON = (By.XPATH, "//table[@id='customer_bookings_table']/tbody/tr[1]/td/a")
    EMPLOYEE_SELECT_DROPDOWN = (By.XPATH, "//select[@id='employee_slot_user_id']")



    # select.select_by_visible_text("Option 1")


    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)


    def go_to_services_page(self):
        self.get_element(self.MANAGE_SERVICES_LINK).click()
        time.sleep(1)




