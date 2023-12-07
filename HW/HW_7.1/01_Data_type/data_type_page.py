from selenium.webdriver.common.by import By

class DataType:
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.set_window_size(1280, 850)
    
    def first_name(self, name):
        firsr_name = self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
        firsr_name.clear()
        firsr_name.send_keys(name)
        
    def last_name(self, name):
        last_name = self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
        last_name.clear()
        last_name.send_keys(name)
         
    def address(self, name):
        addr = self._driver.find_element(By.CSS_SELECTOR, "[name='address']")
        addr.clear()
        addr.send_keys(name)
        
    def zip_code(self, name):
        zip_code = self._driver.find_element(By.CSS_SELECTOR, "[name='zip-code']")
        zip_code.clear()
        zip_code.send_keys(name)
        
    def city(self, name):
        city = self._driver.find_element(By.CSS_SELECTOR, "[name='city']")
        city.clear()
        city.send_keys(name)
        
    def country(self, name):
        country = self._driver.find_element(By.CSS_SELECTOR, "[name='country']")
        country.clear()
        country.send_keys(name)
        
    def email(self, name):
        email = self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
        email.clear()
        email.send_keys(name)
        
    def phone(self, name):
        phone = self._driver.find_element(By.CSS_SELECTOR, "[name='phone']")
        phone.clear()
        phone.send_keys(name)
        
    def job_pos(self, name):
        job_pos = self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
        job_pos.clear()
        job_pos.send_keys(name)
        
    def company(self, name):
        company = self._driver.find_element(By.CSS_SELECTOR, "[name='company']")
        company.clear()
        company.send_keys(name)
        
    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        
        
    def get_first_name_color(self):
        return self._driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
    
    def get_last_name_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")
        
    def get_addr_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
    
    def get_city_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color")
    
    def get_zip_code_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")  
    
    def get_country_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
    
    def get_email_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
    
    def get_phone_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
    
    def get_job_pos_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color")
    
    def get_company_color(self): 
        return self._driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")
    
    
        
    # def check_field_color(self):
    #     color_first_name = self._driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
    #     color_last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")
    #     color_addr = self._driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
    #     color_city = self._driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color")
    #     color_zip_code = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    #     color_country = self._driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
    #     color_email = self._driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
    #     color_phone = self._driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
    #     color_job_pos = self._driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color")
    #     color_company = self._driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")