import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html"))

def login(driver, user, pwd):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(pwd)
    driver.find_element(By.ID, "login").click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "msg"), "i"))
    return driver.find_element(By.ID, "msg").text

def test_login():
    driver = webdriver.Chrome()
    try:
        assert login(driver, "admin", "admin123") == "Login successful"
        assert login(driver, "admin", "wrong") == "Invalid credentials"
    finally:
        driver.quit()
