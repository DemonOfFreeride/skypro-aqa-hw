import allure
from selenium.webdriver.common.by import By

class DataType:
    """
        Этот класс представляет сущность Карточка сотрудника
        У сотрудника есть следующие данные; имя, фамилия, адрес, пчтовый индекс, 
        город проживания, эл. адрес, номер телефона, должность, название компании
    """
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.set_window_size(1280, 850)
    
    
    @allure.step("Поле 'First name'") 
    def first_name(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "First name"
        """
        firsr_name = self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
        firsr_name.clear()
        firsr_name.send_keys(name)


    @allure.step("Поле 'Last name'")         
    def last_name(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "Last name"
        """
        last_name = self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
        last_name.clear()
        last_name.send_keys(name)
        
    @allure.step("Поле 'Address'") 
    def address(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "Address"
        """
        addr = self._driver.find_element(By.CSS_SELECTOR, "[name='address']")
        addr.clear()
        addr.send_keys(name)

    @allure.step("Поле 'Zip code'")         
    def zip_code(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "Zip code"
        """
        zip_code = self._driver.find_element(By.CSS_SELECTOR, "[name='zip-code']")
        zip_code.clear()
        zip_code.send_keys(name)

    @allure.step("Поле 'City'")         
    def city(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "City"
        """
        city = self._driver.find_element(By.CSS_SELECTOR, "[name='city']")
        city.clear()
        city.send_keys(name)

    @allure.step("Поле 'Country'")         
    def country(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "Country"
        """
        country = self._driver.find_element(By.CSS_SELECTOR, "[name='country']")
        country.clear()
        country.send_keys(name)

    @allure.step("Поле 'E-mail'")          
    def email(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "E-mail без символа '@' по середине даннвые не принимаются"
        """
        email = self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
        email.clear()
        email.send_keys(name)

    @allure.step("Поле 'Phone number'")          
    def phone(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "Phone number"
        """
        phone = self._driver.find_element(By.CSS_SELECTOR, "[name='phone']")
        phone.clear()
        phone.send_keys(name)

    @allure.step("Поле 'Job position'")      
    def job_pos(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "Job position"
        """
        job_pos = self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
        job_pos.clear()
        job_pos.send_keys(name)
    
    @allure.step("Поле 'Company'")      
    def company(self, name: str) -> None:
        """
            Функуия вводит данные в ячейку "Company"
        """
        company = self._driver.find_element(By.CSS_SELECTOR, "[name='company']")
        company.clear()
        company.send_keys(name)
    
    @allure.step("Кнопка 'Submit'")      
    def submit(self) -> None:
        """
            Функуия нажимает на кнопку "Submit" для отправки данных на сервер
        """
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()



    @allure.step("Цет поля 'First name'")      
    def get_first_name_color(self) -> str:
        """
            Функция получает цвет ячейки "First name" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
    
    @allure.step("Цет поля 'Last name'")  
    def get_last_name_color(self) -> str:
        """
            Функция получает цвет ячейки "Last name" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")
    
    @allure.step("Цет поля 'Address'")      
    def get_addr_color(self) -> str:
        """
            Функция получает цвет ячейки "Address" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
    
    @allure.step("Цет поля 'City'")  
    def get_city_color(self) -> str:
        """
            Функция получает цвет ячейки "City" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color")
    
    @allure.step("Цет поля 'Zip code'")  
    def get_zip_code_color(self) -> str:
        """
            Функция получает цвет ячейки "Zip code" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")  
    
    @allure.step("Цет поля 'Country'")  
    def get_country_color(self) -> str:
        """
            Функция получает цвет ячейки "Country" после ее заполнения
        """ 
        return self._driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
    
    @allure.step("Цет поля 'E-mail'")  
    def get_email_color(self) -> str:
        """
            Функция получает цвет ячейки "E-mail" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
    
    @allure.step("Цет поля 'Phone number'")  
    def get_phone_color(self) -> str:
        """
            Функция получает цвет ячейки "Phone number" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
    
    @allure.step("Цет поля 'Job positin'")  
    def get_job_pos_color(self) -> str:
        """
            Функция получает цвет ячейки "Job positin" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color")
    
    @allure.step("Цет поля 'Company'")  
    def get_company_color(self) -> str:
        """
            Функция получает цвет ячейки "Company" после ее заполнения
        """
        return self._driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color") 