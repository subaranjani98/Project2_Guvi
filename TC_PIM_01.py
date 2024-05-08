
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

sleep(2)

forgot_password = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
forgot_password.click()

sleep(3)

webelement_username = driver.find_element(By.XPATH, '//input[@name="username"]')
webelement_username.send_keys("Admin")

sleep(3)

reset_password = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
reset_password.click()

sleep(3)

print("Reset Password link sent successfully.")

driver.quit()
