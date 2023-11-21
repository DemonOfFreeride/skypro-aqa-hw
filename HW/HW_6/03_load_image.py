from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Импортируем из селениума функцию "ожидания состояния" 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
driver.set_window_size(1280, 800)


waiter = WebDriverWait(driver, 12) # Ждать 12 секунд

award = waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#award')))  # Ждать до тех пор, пока не появиится элемент с селектором "#award"

print(award.get_attribute('src'))