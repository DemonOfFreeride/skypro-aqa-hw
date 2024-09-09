import allure
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from data_type_page import DataType

@allure.epic("Форма Анкета")
@allure.title("Тест на заполение анкеты")
@allure.description("Пользователь вводит данные в анкету, далее нажимает кнопку Submin после чего программа проверяет правильность ввода данных и что ячейка не пустая")
@allure.severity("blocker")
def test_data_type():
    """
        Функция берет данные идля внесения их в соответствующие поля на веб странице, 
        так же после нажатия на кнопку "Submit" проверяет на факт не заполенных полей
        и на правильность их заполения
    """
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    data_type = DataType(browser)
    # Ввод данных в поля 
    data_type.first_name("Иван")
    data_type.last_name("Петров")
    data_type.address("Ленина, 55-3")
    data_type.zip_code("")
    data_type.city("Москва")
    data_type.country("Россия")
    data_type.email("tests@kypro.com")
    data_type.phone("+7985899998787")
    data_type.job_pos("QA")
    data_type.company("SkyPro")
    data_type.submit()
    
    with allure.step("Проверка на соответсвие цвета ячейки после нажатия на кнопку 'Submit'"):
        full_field = ("rgba(209, 231, 221, 1)") #  заполненное поле - ЗЕЛЕНОЕ
        empty_field = ("rgba(248, 215, 218, 1)") #  пустое поле - КРАССНОЕ
        
        color_check = {
        "first_name": data_type.get_first_name_color(),
        "last_name": data_type.get_last_name_color(),
        "address": data_type.get_addr_color(),
        "zip_code": data_type.get_zip_code_color(),
        "city": data_type.get_city_color(),
        "country": data_type.get_country_color(),
        "email": data_type.get_email_color(),
        "phone": data_type.get_phone_color(),
        "job_position": data_type.get_job_pos_color(),
        "company": data_type.get_company_color(),
        }

        errors = []
        
        for field, expected_color in color_check.items():
            try:
                if expected_color == empty_field:
                    assert expected_color == empty_field, f" * ОШИБКА *  цвет поля - {field} - НЕ СООТВЕТСТВУЕТ ожидаемому цвету (пустое поле)."
                else:
                    assert expected_color == full_field, f" * ОШИБКА *  цвет поля - {field} - НЕ СООТВЕТСТВУЕТ ожидаемому цвету (заполненное поле)."
                print(f"   - ОК - цвет поля - {field} - соответствует ожидаемому цвету.")
            except AssertionError as e:
                error_message = str(e)
                if error_message not in errors:
                    errors.append(error_message)
        
        for error in errors:
            print(error)
    
    sleep(2)
    browser.quit()