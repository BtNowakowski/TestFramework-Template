import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseDriver():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def is_element_visible(self, xpath: str):
        """
        Checks if the element of given xpath is visible on the page
        Args:
            xpath: XPATH of an element on the page

        Returns:
            bool: True if element is visible, False if it's not visible
        """
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except Exception:
            return False

    def click_element(self, xpath: str) -> WebElement:
        """
        Clicks on an element, and returns the WebElement
        Args:
            xpath: XPATH of an element on the page

        Returns:
             WebElement: WebElement at given xpath

        """
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elem.click()
        return elem

