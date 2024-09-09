import allure
from selenium.webdriver.common.by import By

class Calculator:
    """
        Класс калькулятор, имеет простые функции, такие как сложение, вычитание, деление и умножение.
        Операции проводятся как с целыми положительными, отрицательными  так и с дробными числами. 
    """    
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.set_window_size(900, 850)
    
    @allure.step("Ввести целое число для установки отсчета времени в секундах до показа результата операции")    
    def delay(self, time: int) -> None:
        """
            Функция ввода времени задежки в секундах до выдачи результата операции
        """
        delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(time)
    
    @allure.step("Нажать на кнопку что бы очистить результат")    
    def clear_btn(self) -> None:
        """
            Функуия кнопки очистки результата
        """
        self._driver.find_element(By.CSS_SELECTOR, '.clear').click()
    
    @allure.step("Ввести значения от 0 до 9")
    def dig_buttons(self, index: int) -> None:
        """
            Функция нажатия на кнопки цифр от 0 до 9
        """
        dig_buttons = self._driver.find_elements(By.CSS_SELECTOR, '.btn-outline-primary')
        dig_buttons[index].click()
    
    @allure.step("Нажать на кнопку арефметического оператора")
    def operator_buttons(self, index: int) -> None:
        """
            Функция нажатия кнопки операторов "+", "-", "/" и "x" 
        """
        operator_buttons = self._driver.find_elements(By.CSS_SELECTOR, '.btn-outline-success')
        operator_buttons[index].click()
    
    @allure.step("Нажать на кнопку получения результата")    
    def rez_button(self) -> None:
        """
            Функция нажатия на кнопку получения результата операции
        """
        self._driver.find_element(By.CSS_SELECTOR, '.btn-outline-warning').click()
    
    @allure.step("Выдать результат на экране")    
    def rezult(self) -> str:
        """
            Функция получения значения результата операции которое отображено в окне результата
        """        
        return self._driver.find_element(By.CSS_SELECTOR, '.screen').text