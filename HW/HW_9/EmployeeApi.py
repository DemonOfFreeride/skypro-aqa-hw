import requests

class EmployeeApi:
    
    def __init__(self, url):
        self.url = url
        
    def get_company_employee(self, company_id):
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp.json()                     
    
    def get_employee(self, id_employee):
        resp = requests.get(self.url + '/employee/' + str(id_employee))
        return resp.json()