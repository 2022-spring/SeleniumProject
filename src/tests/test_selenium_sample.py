from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest


# @pytest.fixture
# def browser():
#     # initializing the chrome driver
#     return webdriver.Chrome()
#

@pytest.mark.smoke
@pytest.mark.regression
def test_sample_scenario(driver):
    # test scenario starts here
    driver.get("https://www.google.com/")
    time.sleep(5)

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("selenium")
    search_box.send_keys(Keys.ENTER)


@pytest.mark.regression
def test_second_scenario(driver):
    print("This is the sample scenario for pytest")
