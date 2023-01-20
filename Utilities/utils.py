from selenium.webdriver.remote.webelement import WebElement


class Utils:
    def assert_list_of_items(self, value: str, *items: WebElement):
        for item in items:
            print(f"Text of an element: {item.text}")
            assert item.text == value
            print("Assertion completed successfully!")
