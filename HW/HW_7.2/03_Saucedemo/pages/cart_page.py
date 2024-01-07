from selenium.webdriver.common.by import By

class CartPage:
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        
    def go_to_cart_page(self):
        self._driver.get("https://www.saucedemo.com/cart.html")
        
    def back_to_shoping(self):
        self._driver.get("https://www.saucedemo.com/inventory.html")
        
    def del_from_cart_backpack(self):
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-backpack").click()
        
    def del_from_cart_bike_light(self):
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-bike-light").click()

    def del_from_cart_t_shirt(self):
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt").click()

    def del_from_cart_fleece_jacket(self):
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-fleece-jacket").click()

    def del_from_onesie(self):
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-onesie").click()

    def del_from_cart_t_shirt_red(self):
        self._driver.find_element(By.CSS_SELECTOR, "[data-test='remove-test.allthethings()-t-shirt-(red)']").click()