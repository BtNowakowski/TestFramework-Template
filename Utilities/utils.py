import inspect
import logging
import softest
from selenium.webdriver.remote.webelement import WebElement


class Utils(softest.TestCase):
    def assert_list_of_items(self, value: str, *items: WebElement):
        for item in items:
            print(f"Text of an element: {item.text}")
            # if assertion fails test will continue
            self.soft_assert(self.assertEqual(item.text, value))
            if item.text == value:
                print("Assertion completed successfully!")
            else:
                print("Assertion failed")
        self.assert_all()

    def custom_logger(log_level=logging.DEBUG):

        # set class/method name from where its called
        logger_name = inspect.stack()[1][3]

        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        file_handler = logging.FileHandler("../automation.log", mode='w')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger

    def check_if_title_contains_strings(self, page_title: str, strings: list[str]):
        """
        Asserts title of the page to given strings
        Args:
            page_title (str): title to be checked
            strings (list[str]): titles which should title contain
        """

        for string in strings:
            self.soft_assert(self.assertTrue, page_title.upper().__contains__(string.upper()),
                             f"Title doesn't contain \"{string}\"")
        self.assert_all()
