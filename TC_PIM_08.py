from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time



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
    dependent_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
    add_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    name_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    relationship_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    spacify_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    other_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    dateofbirth_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input'
    save_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
    
    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.PIM_locator).click()
        
        

    def dependent(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.serch_locator).send_keys("Gopi Chand Papolu")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.serch_button_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.Edit_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.dependent_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.add_locator).click()
        self.driver.find_element(by=By.XPATH,value=self.name_locator).send_keys("sam")
        self.driver.find_element(by=By.XPATH,value=self.relationship_locator).click()
        self.driver.find_element(by=By.XPATH,value=self.other_locator).send_keys('child')
        
        time.sleep(5)
        #self.driver.find_element(by=By.XPATH,value=self.other_locator).click()
        #self.driver.find_element(by=By.XPATH,value=self.spacify_locator).send_keys("cousin")
        self.driver.find_element(by=By.XPATH,value=self.other_locator).click()
        self.driver.find_element(by=By.XPATH,value=self.dateofbirth_locator).send_keys('2000-04-20')
        self.driver.find_element(by=By.XPATH,value=self.save_locator).click()
        

    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


H=HRM()

H.login()

H.dependent()