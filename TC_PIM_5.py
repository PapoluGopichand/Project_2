# Orange CRM login positive Scenario

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
    Nickname_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    #EmployeId_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
    otherId_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    Driverlicence_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    Expair_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    SSN_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    SIN_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    Nationality_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    Martialstatus_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
    single_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    Date_of_Berth_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    gender_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label'
    Milatary_service_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    Save_button1_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    Bloodtype_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[2]/i'
    Save_button2_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'
    


    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.PIM_locator).click()
        time.sleep(8)
        

    def personaldetails(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.serch_locator).send_keys("Gopi Chand Papolu")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.serch_button_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.Edit_locator).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.Nickname_locator).send_keys("chandu")  
        #self.driver.find_element(by=By.XPATH,value=self.EmployeId_locator).clear().send_keys("1342")  
        self.driver.find_element(by=By.XPATH,value=self.otherId_locator).send_keys("0123")
        self.driver.find_element(by=By.XPATH,value=self.Driverlicence_locator).send_keys("Lafde602")
        self.driver.find_element(by=By.XPATH, value=self.Expair_locator).send_keys('2024-02-03')
        self.driver.find_element(by=By.XPATH,value=self.SSN_locator).send_keys("2341567")
        self.driver.find_element(by=By.XPATH, value=self.SIN_locator).send_keys("4536478")
        self.driver.find_element(by=By.XPATH,value=self.Nationality_locator).send_keys("Indian")
        self.driver.find_element(by=By.XPATH,value=self.Martialstatus_locator).click()
        self.driver.find_element(by=By.XPATH,value=self.single_locator).click()
        self.driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=self.Date_of_Berth_locator).send_keys('1997-01-02')
        self.driver.find_element(by=By.XPATH,value=self.gender_locator).click()
        self.driver.find_element(by=By.XPATH,value=self.Milatary_service_locator).send_keys('No')
        self.driver.find_element(by=By.XPATH,value=self.Save_button1_locator).click()        



    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


H= HRM()

H.login()
H.personaldetails()