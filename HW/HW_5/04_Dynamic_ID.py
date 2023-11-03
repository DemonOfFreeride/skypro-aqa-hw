from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Инициализация драйвера 
driver = webdriver.Chrome()

# Открытие страницы в браузере Google chrome
driver.get("http://uitestingplayground.com/dynamicid")

# Нажать на кнопку "Button with Dynamic ID" 3 раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

sleep(5)


# Инициализация драйвера 
options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://uitestingplayground.com/dynamicid")

# Нажать на кнопку "Button with Dynamic ID" 
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)
driver.quit()


# При перезагрузки страницы, каждый раз изменяется "id" класса "btn btn-primary", нужно это иметь ввиду когда выбираешь селектор для кнопки.
