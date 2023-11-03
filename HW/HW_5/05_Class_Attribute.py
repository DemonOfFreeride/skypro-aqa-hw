from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Инициализация драйвера Selenium
driver = webdriver.Chrome()

# Открытие страницы в браузере Google chrome
driver.get("http://uitestingplayground.com/classattr")

# # Нажать на синию кнопку "Button" 3-и раза, будет ошибка
# for _ in range(3):
#     button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
#     button.click()

driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
sleep(3)

# Инициализация драйвера 
options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://uitestingplayground.com/classattr")

# Нажать на синию кнопку "Button" 
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

time.sleep(3)
driver.quit()

# При новом открытыии или перезагрузки страницы кнопки меняют положение, при этом классы "class1", "class2" и "class3" меняются местами,
# только при нажатии на синюю кнопку всплывает модальное окно.