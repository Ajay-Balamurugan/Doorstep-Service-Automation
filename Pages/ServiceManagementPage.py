import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class ServiceManagementPage(BasePage):
    CREATE_SERVICE_BUTTON = (By.ID, "create")
    TITLE_FIELD = (By.ID, "service_title")
    DESCRIPTION_FIELD = (By.ID, "service_description")
    FILE_FIELD = (By.ID, "service_images")
    SERVICE_FORM_SUBMIT_BUTTON = (By.XPATH, "//form[@id = 'create_service_form']/input[@value='Create Service']")
    MANAGE_OPTIONS_LINK = (By.XPATH, "//h3[contains(text(), 'test_service')]/../../div[@id='service_buttons_container']/a[text()='Manage Service Options']")



    # select.select_by_visible_text("Option 1")


    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)


    def create_service(self, title, description, image_path):
        self.do_click(self.CREATE_SERVICE_BUTTON)
        self.do_send_keys(self.TITLE_FIELD, title)
        self.do_send_keys(self.DESCRIPTION_FIELD, description)
        self.do_send_keys(self.FILE_FIELD, image_path)
        self.do_click(self.SERVICE_FORM_SUBMIT_BUTTON)
        time.sleep(3)

    def go_to_options_page(self):
        self.get_element(self.MANAGE_OPTIONS_LINK).click()
        time.sleep(2)
        return self.current_url()



