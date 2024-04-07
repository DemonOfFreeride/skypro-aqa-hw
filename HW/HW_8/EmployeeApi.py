import requests

class EmployeeApi:
    
    def __init__(self, url):
        self.url = url
        
    def get_company_employee(self, company_id):
        resp = requests.get(self.url + '/emoloyee/' + str(company_id))
        return resp.json() 

    def get_token(self, user='flora', password='nature-fairy'):
        cred = {
            'username': user,
            'password': password      
        }
        
        resp = requests.post(self.url + '/auth/login', json=cred)
        return resp.json()["userToken"]