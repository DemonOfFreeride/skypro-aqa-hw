from selenium.webdriver.common.by import By

class Calculator:
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.set_window_size(900, 850)
        
    def delay(self, time):
        delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(time)
        
    def clear_btn(self):
        self._driver.find_element(By.CSS_SELECTOR, '.clear').click()
        
    def dig_buttons(self, index):
        dig_buttons = self._driver.find_elements(By.CSS_SELECTOR, '.btn-outline-primary')
        dig_buttons[index].click()
    
    def operator_buttons(self, index):
        operator_buttons = self._driver.find_elements(By.CSS_SELECTOR, '.btn-outline-success')
        operator_buttons[index].click()
        
    def rez_button(self):
        self._driver.find_element(By.CSS_SELECTOR, '.btn-outline-warning').click()
        
    def rezult(self):
        return self._driver.find_element(By.CSS_SELECTOR, '.screen').text
    