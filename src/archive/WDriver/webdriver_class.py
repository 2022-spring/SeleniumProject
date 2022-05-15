from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Wdriver package, webdriver_class.py module
# WEDRIVER CLASS
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20) # max wait time for all find element steps

driver.get("https://demoqa.com/browser-windows")
time.sleep(2)

print("# properties for WebDriver class")
print("driver.current_url: ", driver.current_url)
print("driver.current_window_handle: ", driver.current_window_handle)

print("# refresh, back, forward")
driver.back()
driver.refresh()
print("driver.current_url: ", driver.current_url)
driver.forward()
print("driver.current_url: ", driver.current_url)
time.sleep(2)

print("# window handles and multiple windows/tabs ...")
# driver.find_element(By.XPATH, "//button[@id='tabButton']")
# driver.find_element(By.CSS_SELECTOR, "#tabButton")
driver.find_element(By.ID, 'tabButton').click()
time.sleep(2)
print("driver.window_handles: ", driver.window_handles)
print("driver.current_url: ", driver.current_url)

print("## switching to new tab...")
# new_tab_name = driver.window_handles[1]
# driver.switch_to.window(new_tab_name)
driver.switch_to.window(driver.window_handles[-1]) # switching to last tab
print("driver.current_url: ", driver.current_url)
time.sleep(2)

print("## Switching to Alert")
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "promtButton").click()
alrt = driver.switch_to.alert
time.sleep(2)
print("## Clicking the OK...")
alrt.accept()  # clicking OK button

print("## Clicking the cancel...")
time.sleep(2)
driver.find_element(By.ID, "promtButton").click()
alrt = driver.switch_to.alert
alrt.dismiss() # clicking the Cancel button

print("## Entering the text in Alert...")
time.sleep(2)
driver.find_element(By.ID, "promtButton").click()
alrt = driver.switch_to.alert
alrt.send_keys("john doe") # clicking the Cancel button
alrt.accept()
time.sleep(10)

print("Other attributes: ...")
print("driver.name: ", driver.name)
print("driver.title: ", driver.title)

print("# closing the current tab...")
driver.close()
time.sleep(2)
print("# closing the browser!!!!")
driver.quit()
# What is property?
# class Abc():
#     name = ''
#     @property
#     def title(self):
#         return "this is the title"
#
#     @property
#     def title_xpath(self):
#         return f"//div[@id='title-{self.name}']"
#
#     def click_title(self, name):
#         self.name = name
#         driver.find_element(By.XPATH, self.title_xpath)
#
# abc = Abc()
# print(abc.title )
# abc.click_title('dresses')

