import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from Base.base_driver import BaseDriver


@pytest.fixture(scope="class")
def setup(request):

    options = ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.pracuj.pl/")
    driver.maximize_window()
    request.cls.driver = driver

    try:
        bd = BaseDriver(driver)
        bd.wait_for_clickable_element(By.XPATH, '//*[@id="popupContainer"]/div/div/div[1]/button').click()
        bd.wait_for_clickable_element(By.XPATH, '//*[@id="__next"]/div/div[6]/div/div/div/div[4]/div/button[2]').click()
        bd.wait_for_clickable_element(By.XPATH, '//*[@data-test="button-submit"]').click()
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupContainer"]/div/div/div[1]/button'))).click()
        # wait.until(EC.element_to_be_clickable((By.XPATH,
        # '//*[@id="__next"]/div/div[6]/div/div/div/div[4]/div/button[2]'))).click()
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-test="button-submit"]'))).click()
    except BaseException:
        pass

    # Teardown, after test is done
    yield
    driver.close()
