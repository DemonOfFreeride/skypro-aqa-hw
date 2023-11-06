from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Инициализация драйвера 
driver = webdriver.Chrome()

# Открытие страницыв браузере Google chrome
driver.get("http://uitestingplayground.com/dynamicid")

# Нажать на кнопку "Button with Dynamic ID" 5 раз 
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(2)

driver.quit()

# Инициализация драйвера 
options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://uitestingplayground.com/dynamicid")

# Нажать на кнопку "Button with Dynamic ID"  5 раз 
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(2)

driver.quit()


# При перпезагрузки страницы, каждый раз изменяется "id" класса "btn btn-primary", 
# при нажатии на саму кнопку ничего не поисходит, возможно поломана логика кнопки.
