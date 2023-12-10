from selenium.webdriver.common.by import By

class LoginPage:
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()
        
    def user_name(self, user):
        user_name = self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user)
        
    def password(self, pas):
        password = self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(pas)
        
    def login(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()