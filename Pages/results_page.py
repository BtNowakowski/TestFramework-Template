from Base.base_driver import BaseDriver


class ResultPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def check_if_title_contains(self, *titles: str):
        """
        Asserts title of page to given strings
        Args:
            *titles (str): titles to be checked
        """
        for title in titles:
            assert self.get_title().upper().__contains__(title.upper())
