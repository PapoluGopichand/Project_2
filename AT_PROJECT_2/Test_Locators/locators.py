class Orange_Locators :
    #Test_case_1
    #Orange HRM username & password Locators
    username_inputbox = 'username'
    password_inputbox = 'password'
    #Login_button XPath
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    #search_inputbox Xpath
    search_inputbox = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    #Admin Xpath
    admin = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    #PIM Xpath
    pim = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    #Leave Xpath
    leave = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    #Time Xpath
    time = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    #Recruitment Xpath
    recruitment = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    #My Info Xpath
    myinfo = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    #Performance Xpath
    performance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    #Dashboard Xpath
    dashboard = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    #directory Xpath
    directory = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    #Maintenance admin password Xpath
    main_password = '(//*[@type="password"])'
    #Maintenance admin confirm Xpath
    confirm_button = '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]'
    #Maintenance Xpath
    maintenance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    #Buzz XPath
    buzz = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'

    #Test_case_2
    #Admin selection Xpath
    admin = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    #user management Xpath
    user_management = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    #user selection Xpath
    user = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a'
    #user name Xpath
    user_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
    #user role Xpath
    userrole = "(//*[@class='oxd-select-text-input'])[1]"
    #Dropdown Xpath
    drop_down = "(//*[@role='listbox'])"
    #Value Status Xpath
    value_status = "(//*[@class='oxd-select-text-input'])[2]"
    #Status Xpath
    status = "(//*[@class='oxd-select-text-input'])[2]"
    #Dropdown_1 Xpath
    drop_down1 = '(//*[@role="listbox"])'

    #Test_case_3
    #PIM module Xpath
    pim_module = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    #add module Xpath
    add_module = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    #first name Xpath
    employee_firstname = 'firstName'
    #last name XPath
    employee_lastname = 'lastName'
    #create login detials toggle button Xpath
    create_login = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    #create login detial username Xpath
    login_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    #create login detial password Xpath
    login_pword = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    #create login detial confirmation password Xpath
    login_cpword = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    #save button Xpath
    save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    #Test_case_4
    #employee name Xpath
    employee_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    #searching for employee PIM page Xpath
    search_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    #click button Xpath
    click_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div'

    #Test_case_5
    #other id Xpath
    otherid = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    #driver's licence number Xpath
    licence_number = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    #licence expiry date Xpath
    expiry_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    #ssn number Xpath
    ssnnumber = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    #sin number Xpath
    sinnumber = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    #nationality Xpath
    nationality = "(//*[@class='oxd-select-text-input'])[1]"
    #nationality drop-down Xpath
    drop_down2 = "//*[@role='listbox']"
    #marital status Xpath
    marital_status = "(//*[@class='oxd-select-text-input'])[2]"
    #marital status type Xpath
    Status_type = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    #date of birth Xpath
    date_ofbirth = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    #gender Xpath
    gender = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    #military service Xpath
    military_s = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    #save button Xpath
    save_button1 = "(//*[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[1]"

    #Test_case_6
    #contact detial Xpath
    contact_detail ='Contact Details'
    #street Xpath
    street ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    #street name Xpath
    street_n = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    #city name Xpath
    city = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    #state name Xpath
    state = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    #Zip code Xpath
    zcode = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    #country Xpath
    country = "(//*[@class='oxd-select-text-input'])"
    #country drop-down Xpath
    drop_down3 = "//*[@role='listbox']"
    #home number Xpath
    home = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    #mobile number Xpath
    moblie = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    #work name Xpath
    work = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    #work mail id Xpath
    work_mail ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    #other mail id Xpath
    other_mailid = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
    #save button for contact detials
    save_button2 = "(//*[@type='submit'])"

    #Test_case_7
    #emergency contact module Xpath
    emergency_contact = 'Emergency Contacts'
    #assigned emergency contact add button Xpath
    emergency_addbutton = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    #name of emergency contact Xpath
    name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    #relationship of emergency contact Xpath
    relationship = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    #home telephone number Xpath
    home_number =   '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    #mobile number Xpath
    mobile_number = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    #work telephone number Xpath
    work_number = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    #save emergency contact Xpath
    save_button3 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    #Test_case_8
    #dependents button Xpath
    dependent_b = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
    #dependents add button Xpath
    dependents_add = "(//*[@type='button'])[2]"
    #dependents name Xpath
    dependents_n = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    #dependents relationship toogle botton Xpath
    relationship_button = "(//*[@class='oxd-select-text-input'])"
    #dependents date of birth Xpath
    relation_dateob = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input'
    #dependents save button Xpath
    save_button4 = '(//*[@type="submit"])'

    #Test_case_9
    #job button Xpath
    job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    #joined date Xpath
    joined = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    #job tittle Xpath
    job_title = "(//*[@class='oxd-select-text-input'])[1]"
    #job category Xpath
    job_category = "(//*[@class='oxd-select-text-input'])[2]"
    #sub unit Xpath
    sub_unit = "(//*[@class='oxd-select-text-input'])[3]"
    #location Xpath
    location = "(//*[@class='oxd-select-text-input'])[4]"
    #drop-down Xpath
    drop_down = "//*[@role='listbox']"
    #employment status XPath
    employee_status = "(//*[@class='oxd-select-text-input'])[5]"
    #save button Xpath
    save_button5 = '(//*[@type="submit"])'

    #Test_case_10
    #Termination button Xpath
    terminate_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    #Termination date Xpath
    terminate_d = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'
    #Termination reason Xpath
    terminate_reason = "(//*[@class='oxd-select-text-input'])[6]"
    #termination reason drop-down Xpath
    drop_down = "(//*[@role='listbox'])"
    #Termination note Xpath
    note = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea'
    #Termination save button Xpath
    save_button6 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'

    #Test_case_11
    #activation employee Xpath
    activation = '(//*[@type="button"])[2]'

    #Test_case_12
    #salary botton Xpath
    salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a'
    #salary add button Xpath
    salary_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    #salary component Xpath
    salary_com = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    #pay grade Xpath
    pay_grade = "(//*[@class='oxd-select-text-input'])[1]"
    #pay grade and pay frequency drop-down Xpath
    drop_down = "//*[@role='listbox']"
    #pay frequency Xpath
    pay_frequency = "(//*[@class='oxd-select-text-input'])[2]"
    #currency Xpath
    currency = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'

    #salary amount Xpath
    salary_am = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    #include direct deposit setials toggle button Xpath
    toggle_on = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
    #account number Xpath
    account_no = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
    #account type Xpath
    account_type = "(//*[@class='oxd-select-text-input'])[4]"
    #routing number Xpath
    routing_no = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
    #routing amount Xpath
    routing_amount = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'
    #save button Xpath
    save_button7 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'

    #Test_case_13
    #tax button Xpath
    tax = 'Tax Exemptions'
    #fenderal income tax status Xapth
    federal_status = "(//*[@class='oxd-select-text-input'])[1]"
    #drop_down Xpath
    drop_down = "(//*[@role='listbox'])"
    #fendral income tax exmptions Xapth
    fendral_exemptions = '(//*[@class="oxd-input oxd-input--active"])[2]'
    #state income tax exmptions Xapth
    state_income = "(//*[@class='oxd-select-text-input'])[2]"
    #status Xpath
    state_status = "(//*[@class='oxd-select-text-input'])[3]"
    #state income tax exemptions Xpath
    tax_exemptions = '(//*[@class="oxd-input oxd-input--active"])[3]'
    #unemployment state Xpath
    unemployee = "(//*[@class='oxd-select-text-input'])[4]"
    #work state Xpath
    work_state = "(//*[@class='oxd-select-text-input'])[5]"
    #save button Xpath
    save_button8 = "(//*[@type='submit'])"
