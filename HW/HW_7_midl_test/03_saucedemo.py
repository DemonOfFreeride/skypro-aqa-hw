from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/inventory.html')
driver.maximize_window()
sleep(1)

user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
user_name.clear()
user_name.send_keys("standard_user")
sleep(1)

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.clear()
password.send_keys("secret_sauce")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#login-button").click()
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
sleep(1)

driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()
sleep(2)

driver.find_element(By.CSS_SELECTOR, "#checkout").click()
sleep(1)

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.clear()
first_name.send_keys("Luke")
sleep(1)

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.clear()
last_name.send_keys("Skywalker")
sleep(1)

zip = driver.find_element(By.CSS_SELECTOR, "#postal-code")
zip.clear()
zip.send_keys("097791")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#continue").click()
sleep(1)

total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
print(total)

driver.quit()

assert total == "Total: $58.29" , "Не правильтаня общая сумма заказа"