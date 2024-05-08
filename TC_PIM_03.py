from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
sleep(2)

username = "Admin"
password = "admin123"

username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
username_field.send_keys(username)

password_field = driver.find_element(By.XPATH, '//input[@type="password"]')
password_field.send_keys(password)
sleep(3)

login_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
login_button.click()
sleep(3)

menu_option_field = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]').text
print(menu_option_field)
print("The user should be able to see the above-mentioned Admin page Menu Items on Admin Page.")

driver.quit()