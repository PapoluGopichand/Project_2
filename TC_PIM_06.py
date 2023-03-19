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
    contact_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
    Edit_locator='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div'
    street1_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    strret2_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    city_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    state_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    postel_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    country_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i'
    hometelepohe_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    mobile_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    work_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    workemail_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    otheremail_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
    save_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'

    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.PIM_locator).click()
        
        

    def contacts(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.serch_locator).send_keys("Gopi Chand Papolu")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.serch_button_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.Edit_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.contact_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.street1_locator).send_keys("patamati Bhazar")
        self.driver.find_element(by=By.XPATH,value=self.strret2_locator).send_keys("cpm office")
        self.driver.find_element(by=By.XPATH,value=self.city_locator).send_keys("Nandigama")
        self.driver.find_element(by=By.XPATH,value=self.state_locator).send_keys("Andhra Pradesh")
        self.driver.find_element(by=By.XPATH,value=self.postel_locator).send_keys("521182")
        self.driver.find_element(by=By.XPATH,value=self.country_locator).click()
        self.driver.find_element(by=By.XPATH,value=self.country_locator).is_selected('India')
        self.driver.find_element(by=By.XPATH,value=self.hometelepohe_locator).send_keys("9963181997")
        self.driver.find_element(by=By.XPATH,value=self.mobile_locator).send_keys("9963181997")
        self.driver.find_element(by=By.XPATH,value=self.work_locator).send_keys("9963181997")
        self.driver.find_element(by=By.XPATH,value=self.workemail_locator).send_keys("papolugopichand98@gmail.com")        
        self.driver.find_element(by=By.XPATH,value=self.otheremail_locator).send_keys("papolugopichand97@gmail.com")  
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.save_locator).click()



    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)



H=HRM()

H.login()
H.contacts()