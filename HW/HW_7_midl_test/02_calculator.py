from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
driver.set_window_size(900, 850)
sleep(1)

delay = driver.find_element(By.CSS_SELECTOR, '#delay')
delay.clear()
time_dalay = 45
delay.send_keys(time_dalay)
sleep(1)

driver.find_element(By.CSS_SELECTOR, '.clear').click()

buttons = driver.find_elements(By.CSS_SELECTOR, '.btn-outline-primary')
# l_b = len(buttons)
# print(l_b) # Посмотреть длину списка символов

operators = driver.find_elements(By.CSS_SELECTOR, '.btn-outline-success')
# l_o = len(operators)
# print(l_o)  # Посмотреть длинну списка операций

buttons[0].click()
sleep(1)

operators[0].click()
sleep(1)

buttons[1].click()
sleep(1)

driver.find_element(By.CSS_SELECTOR, '.btn-outline-warning').click()
sleep(1)

waiter = WebDriverWait(driver, 1000) # Драйвер ждет много секунд

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'),"15")
)

rez = driver.find_element(By.CSS_SELECTOR, '.screen').text

print(rez)
sleep(2)

driver.quit()

assert rez == "15", "Не правильный ответ"