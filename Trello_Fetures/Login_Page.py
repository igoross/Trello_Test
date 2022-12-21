import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class login_Page(webdriver.Chrome):
    def setUp(self):
        self.driver = webdriver.Chrome()


os.environ['PATH'] += r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
email = "igor0410@futura.edu.rs"
password = "treloautomation"

driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://trello.com/en/login")

enter_email = driver.find_element(By.NAME, "user")
enter_email.send_keys(email)
loginBtn = driver.find_element(By.ID, "login")
loginBtn.click()

enter_pass = WebDriverWait(driver, 1000).until(
    EC.visibility_of_element_located((By.NAME, "password")))
enter_pass.send_keys(password)

click_on_login_btn = driver.find_element(By.ID, "login-submit")
click_on_login_btn.click()

element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "home-sticky-container")))

print(driver.find_element(By.CLASS_NAME, "home-sticky-container").text)

time.sleep(5)
