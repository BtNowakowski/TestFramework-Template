import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def select_position(self, *positions: str):
        """
        Enters all positions given, into positions input
        Args:
            *positions (str): Positions that you look for

        Returns:

        """
        position = self.click_element("//div[@data-test='dropdown-element-kw']//input[@type='text']")
        for pos in positions:
            position.click()
            position.send_keys(pos+","+"\ue007")

    def select_location(self, *locations: str):
        """
        Enters all locations given, into locations input
        Args:
            *locations (str): Locations in which the job will be searched for
        """
        location = self.click_element("//div[@data-test='dropdown-element-wp']//input[@type='text']")

        for loc in locations:
            location.click()
            location.send_keys(loc+","+"\ue007")

    def click_submit(self):
        """
        Simply submits the form
        """
        self.click_element("//button[normalize-space()='Szukaj']")
