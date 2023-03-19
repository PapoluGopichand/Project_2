from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains



class HRM:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "admin123"
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    PIM_locator='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    serch_locator='/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    serch_button_locator='/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    Edit_locator='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div'
    job_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    joindate_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    jobtitle_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
    jobcetagorylocator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'
    subunit_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[2]/i'
    location_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i'
    employement_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]/i'
    contract_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span'
    startdate_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/i'
    enddate_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input'


    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.PIM_locator).click()
        
        

    def job(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.serch_locator).send_keys("Gopi Chand Papolu")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.serch_button_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.Edit_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.job_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.joindate_locator).send_keys("2022-11-02")
        self.driver.find_element(by=By.XPATH,value=self.jobtitle_locator).click()
        time.sleep(5)
        title=self.driver.find_element(by=By.XPATH,value=self.jobtitle_locator)
        select=select(title)
        select.select_by_value('Account Assistant')

        


    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


H=HRM()

H.login()

H.job()