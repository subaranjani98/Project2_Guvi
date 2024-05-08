
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
sleep(3)

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


admin_label = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
admin_label.click()
print("Clicked ADMIN Successfully")
sleep(5)

WebDriverWait(driver, 10).until(EC.title_contains("OrangeHRM"))
sleep(3)

page_title = driver.title
assert page_title == "OrangeHRM", "Validation of title is failed.!"
print("Title is valid")

option_element = driver.find_element(By.XPATH, '//div[@class="oxd-topbar-body"]').text
print(option_element)
print("The user should be able to see the above mentioned Admin page Header on Admin Page.")

driver.quit()
