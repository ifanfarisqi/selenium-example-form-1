from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select 
import time

driver = webdriver.Chrome()

try: 
    driver.get('https://demoqa.com/automation-practice-form')

    # driver.maximize_window()

    driver.find_element(By.ID, 'firstName').send_keys('Ifan Muhammad')
    lastname = driver.find_element(By.ID, 'lastName')
    lastname.send_keys('Muhammad')

    driver.find_element(By.XPATH, '//*[@id="userEmail"]').send_keys('emailifan@gmail.com')

    driver.find_element(By.CSS_SELECTOR, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)').click()

    driver.find_element(By.ID, 'userNumber').send_keys('08263456724')

    driver.find_element(By.ID, 'dateOfBirthInput').clear()
    driver.find_element(By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select').send_keys('Desember')
    driver.find_element(By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select').send_keys('1998')
    driver.find_element(By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[1]').click()

    # driver.find_element(By.ID, 'hobbies-checkbox-3').click()
    # error checkbox

    # driver.find_element(By.XPATH, '//*[@id="subjectsContainer"]/div/div[1]').send_keys('Software Quality Assurance')
    # error field Subject

    driver.find_element(By.ID, 'uploadPicture').send_keys('/Users/ifanmuhammad/selenium-example-form-1/pict-1.jpg')

    driver.find_element(By.ID, 'currentAddress').send_keys('Jl Pengen Jadi SQA No 1')
    

    driver.find_element(By.XPATH, '//*[@id="state"]/div/div[2]/div').click()
    driver.find_element(By.ID, 'react-select-3-input').send_keys('NCR', Keys.RETURN)
    driver.find_element(By.ID, 'react-select-4-input').send_keys('Delhi', Keys.RETURN)

    
    
    driver.find_element(By.ID, 'submit').click()

finally: 
    time.sleep(10)
    # driver.quit()