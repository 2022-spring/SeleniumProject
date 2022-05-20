from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_sample_scenario():
    # initializing the chrome driver
    driver = webdriver.Chrome()

    # test scenario starts here
    driver.get("https://www.google.com/")
    time.sleep(5)

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("selenium")
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    driver.close()

def test_second_scenario():
    print("This is the sample scenario for pytest")

