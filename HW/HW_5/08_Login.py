from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

# Инициализация драйвера Selenium 
driver = webdriver.Chrome()

# Открытие страницы в браузере Google chrome
driver.get("http://the-internet.herokuapp.com/login")

# Заполняем поле "Username"
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
sleep(2)

# Заполняем поле "Password"
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
sleep(2)

# Еажимаем кнопку "Login"
driver.find_element(By.CSS_SELECTOR, "button").send_keys(Keys.RETURN)
sleep(3)


# Инициализация драйвера 
options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://the-internet.herokuapp.com/login")


# Заполняем поле "Username"
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
time.sleep(2)

# Заполняем поле "Password"
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
time.sleep(2)

# Еажимаем кнопку "Login"
driver.find_element(By.CSS_SELECTOR, "button").send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()