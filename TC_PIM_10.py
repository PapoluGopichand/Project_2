from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


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
    termination_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'   
    date_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'
    terminationreson_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[2]/i'
    save_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'

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
        self.driver.find_element(by=By.XPATH,value=self.termination_locator).click()
        self.driver.find_element(by=By.XPATH,value=self.date_locator).send_keys('2023-04-01')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.terminationreson_locator().dropdown)))
        drop_downvalue0=self.driver.find_element(by=By.XPATH, value=self.terminationreson_locator().dropdown).text
        if drop_downvalue0.__contains__("Contract Not Renewed"):
            self.driver.execute_script("var a=arguments[0];a.innerHTML='Contract Not Renewed'")


    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


H=HRM()

H.login()

H.job()