import allure
from selenium.webdriver.common.by import By

class CheckoutPage:
    """
        Класс Страница внесения информации о покупателе, пользователь вводит на странице Имя, а так же адрес доставки. 
    """  
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
    
    @allure.step("Открывается старница для заполнения персональных данных")        
    def go_to_checkout_page(self) -> None:
        """
            Функция открытия страницы заполения персональных данные
        """  
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")
    
    @allure.step("Ввести имя")      
    def first_name(self, f_name: str) -> None:
        """
            Функуия вводит данные в ячейку "First name"
        """
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(f_name)
    
    @allure.step("Ввести фамилию")     
    def last_name(self, l_name: str) -> None:
        """
            Функуия вводит данные в ячейку "Last name"
        """
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(l_name)
    
    @allure.step("Ввести адресс доставки")     
    def zip(self, data: str) -> None:
        """
            Функуия вводит данные в ячейку "Zap/Postal Code"
        """
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(data)
    
    @allure.step("Вернуться на страницу корзины")      
    def back_to_cart(self) -> None:
        """
            Функция перехода со страницы ввода перс. данных на страницу корзины
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "button.back").click()