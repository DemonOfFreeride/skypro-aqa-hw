from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options

# Инициализация драйвера Selenium
driver = webdriver.Chrome()

# Открытие страницы в браузере Google chrome
driver.get("http://uitestingplayground.com/classattr")

# Назатие 3 раза на синюю кнопку вместе с кнопкой "Ok" модального окна
for _ in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
    
    sleep(2) # пауза что бы модальное окно успело появится
    
    alert = Alert(driver)
    alert.accept() # нажатие на кнопку "Ок" модального окна

    sleep(1)

driver.quit()

# Инициализация драйвера 
options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://uitestingplayground.com/classattr")

# Назатие 3 раза на синюю кнопку вместе с кнопкой "Ok" модального окна
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    button.click()
    
    sleep(2) # пауза что бы модальное окно успело появится
    
    alert = Alert(driver)
    alert.accept() # нажатие на кнопку "Ок" модального окна

    sleep(1)

driver.quit()

# При каждом новом открытыии или перезагрузки страницы кнопки меняют положение, 
# при этом меняя классы для кнопок "class1", "class2" или "class3" соответсвенно