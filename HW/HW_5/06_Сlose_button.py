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
sleep(1) 

# Нажать на кнопку "Close" модального окна 
button = driver.find_element(By.CSS_SELECTOR, ".modal-footer p")
button.click()

sleep(3)
