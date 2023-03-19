#we are going to click on forget password link in a login form


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window() #to make large browser window
driver.get("https://rahulshettyacademy.com/client")
time.sleep(3)
#we can find link elements (a href) by link text 
driver.find_element(By.LINK_TEXT,"Forgot password?").click()

time.sleep(3)

#now we going to fill the form
driver.find_element(By.XPATH, "//input[@placeholder='Enter your email address']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys(123456)
driver.find_element(By.XPATH,"//input[@id='confirmPassword']").send_keys(123456)
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Save New Password']").click()
time.sleep(2)