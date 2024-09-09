import allure
from selenium.webdriver.common.by import By

class OverviewPage:
    """
        Класс Страница с общей информацией о сделаном заказе' 
    """ 
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
    
    @allure.step("Открывается старница с общей инфорацией о заказе")           
    def go_to_over_page(self) -> None:
        """
            Функция открытия страницы с общей информацией о заказе
        """  
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")
    
    @allure.step("Сохраняет общую сумму заказа")         
    def get_total(self) -> str:
        """
            Функция получения общей суммы заказа
        """  
        return self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    
    @allure.step("Возврат обратно на страницу с товаром")       
    def back_to_product_page(self) -> None:
        """
            Функция перехода со страницы общей информации о заказе на страницу с перечнем товара
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#cancel").click()
    
    @allure.step("Нажать на кнопку оформления заказа")     
    def finish_shoping(self) -> None:
        """
            Функция нажатия на кннопку оформления заказа
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#finish").click()