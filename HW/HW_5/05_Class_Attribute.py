from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options

# Инициализация драйвера Selenium
driver = webdriver.Chrome()

# Открытие страницы в браузере Google chrome
driver.get("http://uitestingplayground.com/classattr")

# Нажать на синию кнопку "Button" 
button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
button.click()

sleep(3)

# Инициализация драйвера 
options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://uitestingplayground.com/classattr")

# Нажать на синию кнопку "Button" 
button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
button.click()

time.sleep(3)
driver.quit()

# При открытыии или перезагрузки страницы кнопки меняют положение, при этом меняя классы лоя кнопок class1, class2 или class3 соответсвенно