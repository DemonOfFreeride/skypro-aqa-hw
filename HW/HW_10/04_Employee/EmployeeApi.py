import allure
import requests

class EmployeeApi:
    """
        Класс запросов через API
    """  
    
    def __init__(self, url):
        self.url = url
    
    @allure.step("Получить список сотрудников комапнии")        
    def get_company_employee(self, company_id: int) -> list:
        """
            Функция получения списка сотрудников компании
        """  
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp.json()                     
    
    @allure.step("Получить данныее одного сотрудника")   
    def get_employee(self, id_employee: int) -> list:
        """
            Функция получения данныех одного сотрудника
        """  
        resp = requests.get(self.url + '/employee/' + str(id_employee))
        return resp.json()