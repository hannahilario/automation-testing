from selenium import webdriver
import os
import logging
import time
from selenium.webdriver.common.by import By


logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)


class AutomatedTesting:

    """" inti lagi nag-rrun kapag tinawag si AutomatedTesting (class) """
    def __init__(self) -> None:
        """
        Configuration for webdriver
        """
        driver = webdriver.ChromeOptions()
        driver.browser_version = "stable"
        browserPrefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
        driver.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        driver.add_experimental_option("prefs", browserPrefs)
        driver.add_argument("--disable-single-click-autofill")
        driver.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        self.browser = webdriver.Chrome(options=driver)
        logger.info("🚀 web driver configured")

    """ load oo web app"""
    def load_oo_app(self):
        self.browser.get("https://orderonline.dev.dsoftonline.com.au/portal/")
        self.browser.maximize_window()
        logger.info("🌐 OO app")

    """ Action -- sa testing test case like (login)"""
    def login_account(self, account_details):
        email = account_details.get("email")
        password = account_details.get("password")
        time.sleep(3)
        self.browser.find_element(By.ID, "login-nav").click()
        time.sleep(2)
        self.browser.find_element(By.NAME, "email").send_keys(email)
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.XPATH, "//button[@id='login']").click()
        time.sleep(10)  

    """ Action -- sa testing test case like (order)"""
    def add_group_items_with_toppings(self):
        self.browser.find_element(By.ID, "HotandSpicy_207795_213671").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//label[@for='207795-FCP05']").click()
        time.sleep(2)
        # self.browser.find_element(By.XPATH, "//a[normalize-space()='Other']").click()
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,".item.Other").click()
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//label[@for='extra-check-ST12']/span[1]").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//div[@class='col-md-6']//input[@id='207795']").click()
        time.sleep(2)
 
    """ Action -- checkout """
    def checkout(self):
        self.browser.find_element(By.ID, "bt-checkout").click()
        time.sleep(2)
        self.browser.execute_script("window.scrollBy(900, 900);")
        self.browser.find_element(By.XPATH, "//label[@for='payment_type_cash']//img[2]").click()
        time.sleep(4)
        self.browser.find_element(By.XPATH, "//input[@id='pay']").click()
        time.sleep(10)



""" Actual execution --- run test cases"""
at = AutomatedTesting()
at.load_oo_app()

""" TEST-CASE-1 Login """
user = {
    "email": "ezpos.tester1@gmail.com",
    "password": "123123123",
}
at.login_account(user)

""" TEST-CASE-2 add group items with toppings """
at.add_group_items_with_toppings()
at.add_group_items_with_toppings()
at.add_group_items_with_toppings()
at.add_group_items_with_toppings()
at.add_group_items_with_toppings()