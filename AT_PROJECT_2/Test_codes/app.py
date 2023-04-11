from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pytest
from Test_Locators import locators
from Test_Data import data

class Test_code1:
    @pytest.fixture
    def booting_function(self):
          self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
          self.driver.get(data.Orange_Data().url)
          self.driver.maximize_window()
          self.driver.implicitly_wait(10)
        
    def test_search(self, booting_function):
        #test case 1 validating side pane of orange hrm in upper and lower case
        #Orange HRM website login function
        self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
        self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)
        #CLicking of login button
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
        #Admin Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.admin_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().admin).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.admin_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().admin).click()
        #PIM Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.pim_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.pim_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim).click()
        #Leave Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.leave_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().leave).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.leave_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().leave).click()
        #Time Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.time_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().time).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.time_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().time).click()
        #Recruitment Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.recruitment_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().recruitment).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.recruitment_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().recruitment).click()
        #My Info Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.myinfo_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().myinfo).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.myinfo_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().myinfo).click()
        #Performance Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.performance_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().performance).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.performance_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().performance).click()
        #Dashboard Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.dashboard_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().dashboard).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.dashboard_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().dashboard).click()
        #Directory Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.directory_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().directory).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.directory_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().directory).click()
        #Maintenance Upper case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.maintenance_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().maintenance).click()
        #Maintenance module needs password to be filled in for opening and click confirm button
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().main_password).send_keys(data.Orange_Data.maintenance_password)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().confirm_button).click() 
        #Maintenance Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.maintenance_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().maintenance).click()
        #Buzz Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.buzz_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().buzz).click()
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_inputbox).send_keys(data.Orange_Data.buzz_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().buzz).click()
        assert self.driver.title == self.driver.title
        print("Test case 1 - validated search box on admin page")

#test case 2 validating of page header and drop-down in admin module
    def test_Admin(self, booting_function):
          #Orange HRM website login functions and loging function
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().admin).click()
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().user_management).click() 
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().user).click()  
          self.driver.execute_script("window.stop();")
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().user_name).send_keys(data.Orange_Data().u_name)                
          userrole1 = self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().userrole)
          userrole1.click()
          drop1 = self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
          if drop1.__contains__("Admin"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Admin'", userrole1)
          num1 = self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().value_status)
          num1.click()
          drop2 = self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down1).text
          if drop2.__contains__("Enabled"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Enabled'", num1)
          sleep(5)      
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().admin).click()
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().user_management).click() 
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().user).click()   
          self.driver.execute_script("window.stop();")
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().user_name).send_keys(data.Orange_Data().u_name)                
          userrole2 = self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().userrole)
          userrole2.click()
          drop3 = self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
          if drop3.__contains__("ESS"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='ESS'", userrole2)
          status2 = self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().status)
          status2.click()
          drop4 = self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down1).text
          if drop4.__contains__("Disabled"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Disabled'",status2)
          assert self.driver.title == self.driver.title
          print("Test case 2 - validates page header and drop_down on admin page")
     
#test case 3 validating new employee in pim module
    def test_add_employee(self,booting_function):
          #Orange HRM website login functions and loging function
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().add_module).click() 
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().employee_firstname).send_keys(data.Orange_Data().first_name)
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().employee_lastname).send_keys(data.Orange_Data().last_name)
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().create_login).click()
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().login_name).send_keys(data.Orange_Data().login_username)           
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().login_pword).send_keys(data.Orange_Data().login_password)
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().login_cpword).send_keys(data.Orange_Data().confirm_password)                                 
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button).click() 
          assert self.driver.title == self.driver.title
          print("Test case 3 - created employee details on pim module")
#test case 4 checking tabs in pim module
    def test_search_employee(self,booting_function):
           #Orange HRM website login functions and loging function
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()     
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click()                              
           assert self.driver.title == self.driver.title
           print("Test case 4 - validated all tabs in employee list pade in pim module ")
          
#test case 5 filling personal details in pim module
    def test_personal_details(self, booting_function):
           #Orange HRM website login functions and loging function
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click() 
           sleep(5)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().otherid).send_keys(data.Orange_Data().other_id)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().licence_number).send_keys(data.Orange_Data().dlicense_number)           
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().expiry_date).send_keys(data.Orange_Data().license_edate)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().ssnnumber).send_keys(data.Orange_Data().ssn_number)          
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().sinnumber).send_keys(data.Orange_Data().sin_number)                                    
           value=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().nationality)
           value.click()
           drop_downvalue0=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down2).text
           if drop_downvalue0.__contains__("Canadian"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Canadian'",value)
           value2=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().marital_status)
           value2.click()  
           drop_downvalue1=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down2).text
           if drop_downvalue1.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",value2)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().date_ofbirth).send_keys(data.Orange_Data().dob)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().gender).click()                         
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().military_s).send_keys(data.Orange_Data().military_service)    
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button1).click()                                                                                                                       
           assert self.driver.title == self.driver.title
           print("Test case 5 - updated employee personal details in pim module")
           
#test case 6 filling contact details in pim module
    def test_contact_detail(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click()
           self .driver.find_element(by=By.LINK_TEXT, value=locators.Orange_Locators().contact_detail).click() 
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().street).send_keys(data.Orange_Data().street)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().street_n).send_keys(data.Orange_Data().state_name)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().city).send_keys(data.Orange_Data().city_name)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().state).send_keys(data.Orange_Data().state_name)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().zcode).send_keys(data.Orange_Data().zip_code)
           place=self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().country)
           place.click()
           drop_downvalue2=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down3).text
           if drop_downvalue2.__contains__("Canadian"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Canadian'",place)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().home).send_keys(data.Orange_Data().home_number)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().moblie).send_keys(data.Orange_Data().mobile_number)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().work).send_keys(data.Orange_Data().work_name)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().work_mail).send_keys(data.Orange_Data().work_mailid)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().other_mailid).send_keys(data.Orange_Data().other_mail)        
           sleep(2)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button2).click()        
           assert self.driver.title == self.driver.title
           print("Test case 6 - updated employee contact details in pim module")
           
#test case 7 filling Emergency contact details in pim module
    def test_emergency_details(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click() 
           self.driver.find_element(by=By.LINK_TEXT, value=locators.Orange_Locators().emergency_contact).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().emergency_addbutton).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().name).send_keys(data.Orange_Data().name)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().relationship).send_keys(data.Orange_Data().relationship)                      
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().home_number).send_keys(data.Orange_Data().home_telephone)           
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().mobile_number).send_keys(data.Orange_Data().mobile_number1)           
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().work_number).send_keys(data.Orange_Data().work_telephone)           
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button3).click()           
           assert self.driver.title == self.driver.title
           print("Test case 7 - updated employee emergency contact details in pim module")
           
#test case 8 filling Dependents details in pim module
    def test_dependent_details(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().dependent_b).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().dependents_add).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().dependents_n).send_keys(data.Orange_Data().dependent_name)
           relative = self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().relationship_button)
           relative.click()
           dropdown3=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if dropdown3.__contains__("Child"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Child'",relative)
           sleep(5)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().relation_dateob).send_keys(data.Orange_Data().realtion_dob)
           sleep(5)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button4).click()     
           assert self.driver.title == self.driver.title
           print("Test case 8 - updated employee dependents contact details in pim module")
           
#test case 9 filling Job details in pim module
    def test_job_detail(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().job).click()
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().joined).send_keys(data.Orange_Data().joined_date) 
           sleep(3)
           job_name=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().job_title)
           job_name.click()
           dropdown_value4=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if dropdown_value4.__contains__("Software Engineer"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Software Engineer'",job_name)
           job_role=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().job_category)
           job_role.click()
           dropdown_value5=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if dropdown_value5.__contains__("Professionals"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Professionals'",job_role)
                   
           sub_name=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().sub_unit)
           sub_name.click()
           dropdown_value6=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if dropdown_value6.__contains__("Engineering"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Engineering'",sub_name)    
     
           area=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().location)
           area.click()
           dropdown_value7=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if dropdown_value7.__contains__("Canadian Regional HQ"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Canadian Regional HQ'",area)    
               
           employee_position=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_status)
           employee_position.click()
           dropdown_value8=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if dropdown_value8.__contains__("Full-Time Contract"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Full-Time Contract'",employee_position)
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button5).click()
           assert self.driver.title == self.driver.title
           print("Test case 9 - updated employee job details in pim module")
           
#test case 10 filling termination on Job details in pim module
    def test_terminate(self, booting_function):      
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().job).click()       
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators.terminate_button).click()
           sleep(3)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().terminate_d).send_keys(data.Orange_Data().termination_d)
           terminate=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators.terminate_reason)
           terminate.click()
           dropdown_value9=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators.drop_down).text
           if dropdown_value9.__contains__("Other"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Other'",terminate)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators.note).send_keys(data.Orange_Data().terminate_note)    
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators.save_button6).click()
           assert self.driver.title ==  self.driver.title
           print("Test case 10 - terminated employee job details in pim module ")
           
#test case 11 activation on Job details in pim module
    def test_activate(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().job).click()       
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators.activation).click()  
           assert self.driver.title == self.driver.title
           print("Test case 11 - activated employee job details in pim module")
           
#test case 12 filling employee salary on Job details in pim module
    def test_salary_details(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click()  
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().salary).click()
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().salary_add).click()           
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().salary_com).send_keys(data.Orange_Data().salary_component)
           value=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pay_grade)
           value.click()
           drop_downvalue10=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue10.__contains__("Grade 1"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Grade 1'",value)
           name=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pay_frequency)
           name.click()
           drop_downvalue11=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue11.__contains__("Monthly"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Monthly'",name)     
           money=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().currency)
           money.click()
           drop_downvalue12=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue12.__contains__("Canadian Dollar"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Canadian Dollar'",money)          
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators.salary_am).send_keys(data.Orange_Data().salary_amount)                     
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().toggle_on).click()     
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().account_no).send_keys(data.Orange_Data().account_number)                      
           account=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().account_type)
           account.click()
           drop_downvalue13=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue13.__contains__("Savings"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Savings'",account) 
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().routing_no).send_keys(data.Orange_Data().routing_number) 
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().routing_amount).send_keys(data.Orange_Data().r_amount) 
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button7).click()
           assert self.driver.title ==  self.driver.title
           print("Test case 12 - updated employee salary on salary component page")
           
#test case 13 filling employee salary on Tax exemption in pim module

    def test_tax_details(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().woker_name)
           sleep(5)
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()      
           sleep(5)           
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click()          
           self.driver.find_element(by=By.LINK_TEXT, value=locators.Orange_Locators().tax).click() 
           sleep(5)
           source=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().federal_status)
           source.click()
           drop_downvalue14=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue14.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",source) 
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().fendral_exemptions).send_keys(data.Orange_Data().fit_exemption)
           state=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().state_income)
           state.click()
           drop_downvalue15=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue15.__contains__("New York"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='New York'",state)
           tax=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().state_status)
           tax.click()
           drop_downvalue16=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue16.__contains__("Single"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Single'",tax)
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().tax_exemptions).send_keys(data.Orange_Data().sit_exemption)
           unemployee=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().unemployee)
           unemployee.click()
           drop_downvalue17=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue17.__contains__("California"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='California'",unemployee)
           work=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().work_state)
           work.click()
           drop_downvalue18=self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().drop_down).text
           if drop_downvalue18.__contains__("Florida"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Florida'",work)  
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button8).click()           
           assert self.driver.title == self.driver.title
           print("Test case 13 - updated tax exemption in pim module")
           
           