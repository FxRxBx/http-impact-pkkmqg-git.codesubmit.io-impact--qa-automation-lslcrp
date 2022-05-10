from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/Users/fxrxbx/Downloads/chromedriver')

driver.get("https://qa-challenge.codesubmit.io/")

element = driver.find_element(By.ID, "user-name")
element.clear()
element.send_keys("performance_glitch_user")
time.sleep(1)

element = driver.find_element(By.ID, "password")
element.clear()
element.send_keys("secret_sauce")
time.sleep(1)

element = driver.find_element(By.ID, "login-button")
element.click()