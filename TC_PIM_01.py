
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time


class HRM:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait = WebDriverWait(driver,5)
    username = "Admin"
    password = "admin123"
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    serch_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'

    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()


    def serch(self):
        try:
            serch_locator=self.driver.find_element(by=By.XPATH, value=self.serch_locator)
            self.driver.find_element(by=By.XPATH, value=self.serch_locator).click()
            self.driver.find_element(by=By.XPATH, value=self.serch_locator).send_keys("Admin")
            action= ActionChains(self.driver)
            action.double_click(on_element= serch_locator).double_click().send_keys("PIM").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("Leave").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("Time").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("Recruitment").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("My info").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("Perfomence").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("Dashboard").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("Directory").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("Maintenance").perform()
            action.double_click(on_element= serch_locator).double_click().send_keys("Buzz").perform()
        finally:
            self.driver.quit()



    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


H= HRM()

H.login()
H.serch()