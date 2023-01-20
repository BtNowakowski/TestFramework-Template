import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver():
    def __init__(self, driver):
        self.driver = driver

    def is_element_visible(self, locator_type: str, locator: str):
        """
        Checks if the element of given xpath is visible on the page
        Args:
            locator_type: type of the locator

            locator:  locator of an element on the page

        Returns:
            bool: True if element is visible, False if it's not visible
        """
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.visibility_of_element_located((locator_type, locator)))
            return True
        except Exception:
            return False

    def wait_for_clickable_element(self, locator_type: str, locator: str) -> WebElement:
        """
            Returns the WebElement
        Args:
            locator_type: type of the locator

            locator:  locator of an element on the page

        Returns:
            web_elem: WebElement at given locator
        """
        wait = WebDriverWait(self.driver, 10)
        web_elem = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return web_elem

