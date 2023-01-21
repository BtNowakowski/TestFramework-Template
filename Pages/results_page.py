from Base.base_driver import BaseDriver
import logging
import softest


from Utilities.utils import Utils


class ResultPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
