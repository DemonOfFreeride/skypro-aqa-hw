import allure
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from calculator_page import Calculator

@allure.epic("Калькулятор")
@allure.title("Проверка операции сложения")
@allure.description("Пользователь складывает на калькуляторе два простых числа, результат выводится на экран нажанию на кнопку '='")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    calculator = Calculator(browser)
    
    # матрица кнопок с цифрами и точкой {цифра: индекс}
    digit_mapping = {
        7: 0,
        8: 1,
        9: 2,
        4: 3,
        5: 4,
        6: 5,
        1: 6,
        2: 7,
        3: 8,
        0: 9,
        "dot": 10
    }
    
    # матрица кнопок операторов {оператор: индекс}
    operator_mapping = {
        "+": 0,
        "-": 1,
        "/": 2,
        "x": 3 
    }   
    
    delay = 4
    calculator.delay(delay) # Задержка вывода результата в сек.
    calculator.clear_btn()
    
    # нажать на кнопку "7"
    digit = 7
    with allure.step(f"Ввели значение '{digit}'"):
        index = digit_mapping.get(digit)
        calculator.dig_buttons(index)
    
    # нажать на кнопку "+"
    operator = "+"
    with allure.step(f"Нажали на кнопку оператора '{operator}'"):
        index = operator_mapping.get(operator)
        calculator.operator_buttons(index)
    
    # нажать на кнопку "8"
    digit = 8 
    with allure.step(f"Ввели значение '{digit}'"):
        index = digit_mapping.get(digit)
        calculator.dig_buttons(index)
    
    calculator.rez_button()  
    
    expected_rezult = "15" # вввести значение которое ожидаете увидеть в ответе
    
    waiter = WebDriverWait(browser, 50) # Драйвер ждет 50 секунд, или до момента появления результата на экране
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), expected_rezult)
    ) 
    
    rez = calculator.rezult()
    with allure.step(f"Результат операции: '{rez}'"):
        print(f"Резулатат на экране калькулятора - {rez}") # вывести на экран результат выданный в калькуляторе

    browser.quit()
    with allure.step("Проверить, результат соответсвует ожидаемому результату"):
        assert rez ==  expected_rezult,  "Не правильный ответ"