from selenium.webdriver.common.by import By

class CheckoutPage:
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        
    def go_to_checkout_page(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")
        
    def first_name(self, f_name):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(f_name)
        
    def last_name(self, l_name):
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(l_name)
        
    def zip(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(data)
        
    def back_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "button.back").click()