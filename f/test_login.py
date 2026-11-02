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

# ---------------- STEPS (f) Web Application Testing Using Selenium ----------------
# 1. pip install selenium pytest   (Chrome must be installed)
# 2. login.html = employee portal login page (admin / admin123)
# 3. Open page with webdriver.Chrome() and driver.get(URL)
# 4. Fill username/password with find_element(By.ID, ...).send_keys()
# 5. Click login, use WebDriverWait + expected_conditions (explicit wait)
# 6. assert "Login successful" for valid, "Invalid credentials" for wrong password
# 7. Run: cd f && pytest -v test_login.py
