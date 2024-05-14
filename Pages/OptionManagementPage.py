import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class OptionManagementPage(BasePage):
    CREATE_OPTION_BUTTON = (By.XPATH, "//button[contains(text() , 'Create Option')]")
    TITLE_FIELD = (By.ID, "option_title")
    DESCRIPTION_FIELD = (By.ID, "option_description")
    DURATION_FIELD = (By.ID, "option_duration")
    PRICE_FIELD = (By.ID, "option_price")
    OPTION_FORM_SUBMIT_BUTTON = (By.XPATH, "//form[@id = 'create_option_form']/input[@value='Create Option']")

    UPDATE_OPTION_BUTTON = (By.XPATH, "//h5[contains(text(),'test_option_1')]/../div/button[contains(text(),'Update Option')]")
    EDIT_TITLE_FIELD = (By.XPATH, "//h5[contains(text(),'test_option_1')]/../div/button[contains(text(),'Update Option')]/following-sibling::div//input[@name='option[title]']")
    EDIT_DESCRIPTION_FIELD = (By.XPATH, "//h5[contains(text(),'test_option_1')]/../div/button[contains(text(),'Update Option')]/following-sibling::div//textarea[@name='option[description]']")
    EDIT_DURATION_FIELD = (By.XPATH, "//h5[contains(text(),'test_option_1')]/../div/button[contains(text(),'Update Option')]/following-sibling::div//input[@name='option[duration]']")
    EDIT_PRICE_FIELD = (By.XPATH, "//h5[contains(text(),'test_option_1')]/../div/button[contains(text(),'Update Option')]/following-sibling::div//input[@name='option[price]']")
    UPDATE_OPTION_FORM_SUBMIT_BUTTON = (By.XPATH, "//h5[contains(text(),'test_option_1')]/../div/button[contains(text(),'Update Option')]/following-sibling::div//input[@value='Update Option']")

    ADMIN_DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")



    # select.select_by_visible_text("Option 1")Update Option


    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)


    def create_option(self, title, description, duration, price):
        self.do_click(self.CREATE_OPTION_BUTTON)
        self.do_send_keys(self.TITLE_FIELD, title)
        self.do_send_keys(self.DESCRIPTION_FIELD, description)
        self.do_send_keys(self.DURATION_FIELD, duration)
        self.do_send_keys(self.PRICE_FIELD, price)
        self.do_click(self.OPTION_FORM_SUBMIT_BUTTON)
        time.sleep(2)

    def update_option(self, title, description, duration, price):
        self.do_click(self.UPDATE_OPTION_BUTTON)
        # Reset the edit fields
        self.do_clear(self.EDIT_TITLE_FIELD)
        self.do_clear(self.EDIT_DESCRIPTION_FIELD)
        self.do_clear(self.EDIT_DURATION_FIELD)
        self.do_clear(self.EDIT_PRICE_FIELD)
        # Now you can send keys to the edit fields
        self.do_send_keys(self.EDIT_TITLE_FIELD, title)
        self.do_send_keys(self.EDIT_DESCRIPTION_FIELD, description)
        self.do_send_keys(self.EDIT_DURATION_FIELD, duration)
        self.do_send_keys(self.EDIT_PRICE_FIELD, price)

        self.do_click(self.UPDATE_OPTION_FORM_SUBMIT_BUTTON)

    def go_to_admin_dashboard_page(self):
        self.get_element(self.ADMIN_DASHBOARD_LINK).click()
        time.sleep(1)




