import os
import time
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
from Base.base_driver import BaseDriver
from Utilities.utils import Utils
driver = None

@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    global driver
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.rcvacademy.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Test Automation Report"
