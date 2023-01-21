from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.utils import Utils
from selenium.common.exceptions import NoSuchElementException


class BaseDriver():
    def __init__(self, driver):
        self.driver = driver

    log = Utils.custom_logger()
    ut = Utils()

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
        except NoSuchElementException:
            return False

    def get_visible_elements(self, locator_type: str, locator: str) -> list[WebElement]:
        wait = WebDriverWait(self.driver, 10)
        web_elem = wait.until(EC.visibility_of_all_elements_located((locator_type, locator)))
        return web_elem

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

    def get_title(self):
        self.log.info("Get title\n")
        return self.driver.title

    def check_if_page_title_contains(self, strings: list[str]):
        title = self.get_title()

        for tt in strings:
            self.log.info(f"String to be tested: {tt}")
            if title.upper().__contains__(tt.upper()):
                self.log.info(f"Assertion completed successfully! Title contains {tt}\n")
            else:
                self.log.critical(f"Assertion failed Title doesn't contain {tt}\n")

        self.ut.check_if_title_contains_strings(title, strings)

