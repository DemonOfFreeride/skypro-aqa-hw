from selenium.webdriver.common.by import By

class OverviewPage:
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        
    def go_to_over_page(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")
        
    def get_total(self):
        return self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        
    def back_to_product_page(self):
        self._driver.find_element(By.CSS_SELECTOR, "#cancel").click()
        
    def finish_shoping(self):
        self._driver.find_element(By.CSS_SELECTOR, "#finish").click()