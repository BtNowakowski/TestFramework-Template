import pytest

from Base.base_driver import BaseDriver


class ResultPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_title(self, *titles: str):
        for title in titles:
            flag = self.driver.title.__contains__(title)
        assert flag
