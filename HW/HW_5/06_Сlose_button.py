from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Инициализация драйвера Selenium 
driver = webdriver.Chrome()

# Открытие страницы в браузере Google chrome
driver.get("http://the-internet.herokuapp.com/entry_ad")

# нужна пауза, т.к. следующая команда не успевает найти кнопку в модальном окне из за его задержки при появлении
sleep(2) 

# Нажать на кнопку "Close" модального окна 
driver.find_element(By.CSS_SELECTOR, ".modal-footer p").click()

sleep(3)


# Инициализация драйвера 
options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://the-internet.herokuapp.com/entry_ad")

# нужна пауза, т.к. следующая команда не успевает найти кнопку в модальном окне из за его задержки при появлении
time.sleep(2)

# Нажать на кнопку "Close" модального окна 
driver.find_element(By.CSS_SELECTOR, ".modal-footer p").click()

time.sleep(3)
driver.quit()