from selenium.webdriver.common.by import By

class ProductPage:
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        
    def go_to_prod_page(self):
        self._driver.get("https://www.saucedemo.com/inventory.html")