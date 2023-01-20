import pytest

from Base.base_driver import BaseDriver


class ResultPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_title(self, *titles: str):
        """
        Asserts title of page to given strings
        Args:
            *titles (str): titles to be checked
        """
        for title in titles:
            flag = self.driver.title.__contains__(title)
        assert flag
