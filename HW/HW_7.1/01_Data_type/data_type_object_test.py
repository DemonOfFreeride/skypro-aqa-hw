from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from data_type_page import DataType

def test_data_type():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    data_type = DataType(browser)
    # Ввод данных в поля 
    data_type.first_name("Иван")
    data_type.last_name("Петров")
    data_type.address("Ленина, 55-3")
    data_type.zip_code("")
    data_type.city("Москва")
    data_type.country("Россия")
    data_type.email("test@skypro.com")
    data_type.phone("+7985899998787")
    data_type.job_pos("QA")
    data_type.company("SkyPro")
    data_type.submit()
    
    # Проверка на соответсвие цета поля: заполненное - ЗЕЛЕНОЕ, пустое - КРАССНОЕ
    full_field = ("rgba(209, 231, 221, 1)") 
    empty_field = ("rgba(248, 215, 218, 1)")
    
    
    
    
    
    sleep(2)
    browser.quit()