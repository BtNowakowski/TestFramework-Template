import pytest

from Base.base_driver import BaseDriver


class ResultPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def check_title(self, *titles: str):
        for title in titles:
            flag = self.driver.title.__contains__(title)
        assert flag
