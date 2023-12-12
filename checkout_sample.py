from selenium import webdriver
import os
import logging
import time
from selenium.webdriver.common.by import By

logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.environ.get("HOMEDRIVE").replace("\\","/") + os.environ.get("HOMEPATH").replace("\\","/") + "/Desktop/testLog.txt")
logger.addHandler(handler)

browserOpts = webdriver.ChromeOptions()
browserOpts.browser_version = "stable"
browserPrefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
browserOpts.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
browserOpts.add_experimental_option("prefs", browserPrefs)
browserOpts.add_argument("--disable-single-click-autofill")
browserOpts.set_capability("goog:loggingPrefs", {"performance": "ALL"})
browser = webdriver.Chrome(options=browserOpts)
browser.get("https://orderonline.dev.dsoftonline.com.au/portal/")
browser.maximize_window()
time.sleep(3)
browser.find_element(By.ID, "login-nav").click()
time.sleep(2)
browser.find_element(By.NAME, "email").send_keys("ezpos.tester1@gmail.com")
browser.find_element(By.ID, "password").send_keys("123123123")
browser.find_element(By.XPATH, "//button[@id='login']").click()
time.sleep(10)
## add item
browser.find_element(By.ID, "HotandSpicy_207795_213671").click()
time.sleep(2)
browser.find_element(By.XPATH, "//label[@for='207795-FCP05']").click()
browser.find_element(By.XPATH, "//a[normalize-space()='Other']").click()
time.sleep(1)
browser.find_element(By.CSS_SELECTOR,".item.Other").click()
time.sleep(1)
browser.find_element(By.XPATH, "//label[@for='extra-check-ST12']/span[1]").click()
time.sleep(2)
browser.find_element(By.XPATH, "//div[@class='col-md-6']//input[@id='207795']").click()
time.sleep(2)
browser.find_element(By.ID, "bt-checkout").click()
time.sleep(2)
browser.execute_script("window.scrollBy(900, 900);")
browser.find_element(By.XPATH, "//label[@for='payment_type_cash']//img[2]").click()
time.sleep(4)
browser.find_element(By.XPATH, "//input[@id='pay']").click()
time.sleep(10)
