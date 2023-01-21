# import time
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Pages.results_page import ResultPage


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    POSITION_INPUT_FIELD = "//div[@data-test='dropdown-element-kw']//input[@type='text']"
    LOCATION_INPUT_FIELD = "//div[@data-test='dropdown-element-wp']//input[@type='text']"
    SUBMIT_BUTTON = "//button[normalize-space()='Szukaj']"

    def get_position_input_field(self) -> WebElement:
        return self.wait_for_clickable_element(By.XPATH, self.POSITION_INPUT_FIELD)

    def get_location_input_field(self) -> WebElement:
        return self.wait_for_clickable_element(By.XPATH, self.LOCATION_INPUT_FIELD)

    def get_submit_button(self) -> WebElement:
        return self.wait_for_clickable_element(By.XPATH, self.SUBMIT_BUTTON)

    def clear_position_input_field(self):
        self.get_position_input_field().click()
        self.get_position_input_field().send_keys(Keys.CONTROL + "a")
        self.get_position_input_field().send_keys(Keys.DELETE)

    def clear_location_input_field(self):
        self.get_location_input_field().click()
        self.get_location_input_field().send_keys(Keys.CONTROL + "a")
        self.get_location_input_field().send_keys(Keys.DELETE)

    def enter_position(self, *positions: str):
        """
        Enters all positions given, into positions input
        Args:
            *positions (str): Positions that you look for
        """
        for pos in positions:
            self.get_position_input_field().click()
            self.get_position_input_field().send_keys(pos + "," + Keys.ENTER)

    def enter_location(self, *locations: str):
        """
        Enters all locations given, into locations input
        Args:
            *locations (str): Locations in which the job will be searched for
        """
        for loc in locations:
            self.get_location_input_field().click()
            self.get_location_input_field().send_keys(loc + "," + Keys.ENTER)

    def click_submit_button(self):
        """
        Simply submits the form
        """
        self.get_submit_button().click()

    def clear_fields(self):
        self.clear_location_input_field()
        self.clear_position_input_field()

    def search_for_job(self, positions: list[str], locations: list[str]) -> ResultPage:
        """
        Method which enters all information given into input fields, submits, and clears the form
        Args:
            positions (list[str]): positions to be entered
            locations (list[str]): locations to be entered
        """
        self.enter_position(*positions)
        self.enter_location(*locations)
        self.click_submit_button()
        self.clear_fields()
        job_search_results = ResultPage(self.driver)
        return job_search_results

