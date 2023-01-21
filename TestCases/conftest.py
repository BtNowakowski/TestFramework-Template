import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from Base.base_driver import BaseDriver
from Utilities.utils import Utils


@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        print("--browser parameter should be equal to chrome, firefox or edge")
        raise ValueError("Invalid browser parameter!")

    driver.get(url)
    # "https://www.pracuj.pl/"
    driver.maximize_window()
    request.cls.driver = driver

    try:
        bd = BaseDriver(driver)
        bd.wait_for_clickable_element(By.XPATH, '//*[@id="popupContainer"]/div/div/div[1]/button').click()
        bd.wait_for_clickable_element(By.XPATH, '//*[@id="__next"]/div/div[6]/div/div/div/div[4]/div/button[2]').click()
        bd.wait_for_clickable_element(By.XPATH, '//*[@data-test="button-submit"]').click()
    except NoSuchElementException:
        log = Utils.custom_logger()
        log("No cookies to be declined")

    # Teardown, after test is done
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")
