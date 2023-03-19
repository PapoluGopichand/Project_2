from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from TC_PIM_03 import HRM


class validation:
    personal_details_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'


def check(self):
    self.driver.find_element(by=By.XPATH, value=self.personal_detail_locator).isDisplayed()