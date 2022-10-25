from ast import While
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException,StaleElementReferenceException

import time

def Bot(username, password, address,city,name,country, state,zip, state_check=False):

    driver= webdriver.Chrome(executable_path="chromedriver_win32\chromedriver.exe")
    driver.get("https://shopify.dev/")

    check = True
    while check:
        try:
            driver.find_element('xpath',"//*[@id='ShopifyMainNav']/div[2]/ul[2]/li[2]/a").click()
            check=False
        except NoSuchElementException:
            print("element not available")
            time.sleep(1)
            check =True


    driver.find_element('xpath','//*[@id="account_email"]').send_keys(username)

    check = True
    while check:
        try:    
            driver.find_element('xpath','//*[@id="body-content"]/div[2]/div/div[2]/div/div/div[2]/div/form/button').click() # email continue button 
            check = False
        except ElementClickInterceptedException:
            print("element not active")
            time.sleep(1)
            check = True

    check = True
    while check:
        try:
            driver.find_element('xpath','//*[@id="account_password"]').send_keys(password)
            check = False
        except ElementNotInteractableException:
            print("login button not available")
            time.sleep(1)
            check = True
        except StaleElementReferenceException:
            print("login button not available")
            time.sleep(1)
            check = True       



    check = True
    while check:
        try:
            driver.find_element('xpath','//*[@id="login_form"]/div[2]/ul/button').click()
            check = False
        except ElementClickInterceptedException:
            print("element not active")
            time.sleep(1)
            check = True


    driver.find_element('xpath','//*[@id="AppFrameAside"]/div[1]/div[2]/div/div/nav/ul[1]/li[1]/a/span').click()

    check= True
    while check:
        try:
            driver.find_element('xpath','//*[@id="AppFrameMain"]/div/div[1]/div[1]/div/div[2]/a/span/span').click()
            check=False
        except ElementNotInteractableException:
            print("login button not available")
            check = True
        except StaleElementReferenceException:
            print("login button not available")
            time.sleep(1)
            check = True 
        except NoSuchElementException:
            time.sleep(1)
            check = True
    check=True
    while check:
        try:
            driver.find_element('xpath','//*[@id="PolarisChoiceList1"]/ul/li[1]/div/label/span[2]').click()
            check=False
        except StaleElementReferenceException:
            print("login button not available")
            time.sleep(1)
            check = True 
        except NoSuchElementException:
            time.sleep(1)
            check = True


    driver.find_element('xpath','//*[@id="PolarisTextField1"]').send_keys(name)

    


    driver.find_element('xpath','//*[@id="PolarisTextField4"]').send_keys(password)
    driver.find_element('xpath','//*[@id="PolarisTextField5"]').send_keys(password)


    check=True
    while check:
        try:
            Country=Select(driver.find_element(By.ID,'PolarisSelect1'))#selecting country
            Country.select_by_visible_text(country)
            check=False
        except NoSuchElementException:
            time.sleep(1)
            check=True


    while state_check:
        try:
            State=Select(driver.find_element(By.ID,'PolarisSelect2'))#selecting state
            State.select_by_visible_text(state)
            state_check=False
        except NoSuchElementException:
            time.sleep(1)
            state_check=False
        except NotImplementedError:
            time.sleep(10)
            state_check=False
            ("state is disabled")
            



    for i in range(150):
        driver.find_element(By.XPATH,'//*[@id="PolarisTextField6"]').send_keys(Keys.BACK_SPACE)#Address

    driver.find_element(By.XPATH,'//*[@id="PolarisTextField6"]').send_keys(address) #Address

    for i in range(60):
        driver.find_element(By.XPATH,'//*[@id="PolarisTextField7"]').send_keys(Keys.BACK_SPACE)#City

    driver.find_element(By.XPATH,'//*[@id="PolarisTextField7"]').send_keys(city) #City
    for i in range(20):
        driver.find_element(By.XPATH,'//*[@id="PolarisTextField8"]').send_keys(Keys.BACK_SPACE)#zip
    driver.find_element(By.XPATH,'//*[@id="PolarisTextField8"]').send_keys(zip) #Zip 

    #region needs to be implemented
    time.sleep(1)


    driver.find_element('xpath','//*[@id="signup_source_details"]/ul/li[1]/label/span[1]/span/span[1]').click() #Build a new store for a client

    driver.find_element('xpath','//*[@id="AppFrameMain"]/div/div/div[2]/div[2]/div/div/div[2]/button').click() # save

    time.sleep(10)


    driver.close()
