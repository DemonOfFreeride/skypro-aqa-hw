import allure
from selenium.webdriver.common.by import By

class LoginPage:
    """
        Класс Страница логинации, пользователь вводит логин и пароль в соответсвующие поля.
        после чего наживает на кнопку 'Login'. 
    """  
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()
       
    @allure.step("Ввести логин")    
    def user_name(self, user: str) -> None:
        """
            Функция ввода данных в поле 'Username'
        """   
        user_name = self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user)
    
    @allure.step("Ввести пароль")  
    def password(self, pas: str) -> None:
        """
            Функция ввода данных в поле 'Password'
        """     
        password = self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(pas)
    
    @allure.step("Нажать на кнопку 'Login'")      
    def login(self) -> None:
        """
            Функция нажатия на кнопку 'Login'
        """  
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()