from selenium.webdriver.common.by import By

class ProductPage:
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        
    def go_to_prod_page(self):
        self._driver.get("https://www.saucedemo.com/inventory.html")
        
    def add_to_cart_backpack(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    def add_to_cart_bike_light(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()       
    
    def add_to_t_shirt(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        
    def add_to_cart_fleece_jacket(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket").click()
        
    def add_to_cart_onesie(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        
    def add_to_cart_t_shirt_red(self):
        self._driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']").click()