import requests
from faker import Faker
fake = Faker('ru_RU')

class EmployeeApi:
    
    def __init__(self, url):
        self.url = url
        
    def create_new_data(self):
        requests.get(self.url + '/test-data')

    def get_company_list(self):
        resp = requests.get(self.url + '/company')
        return resp.json() 
    
    def get_token(self, user='flora', password='nature-fairy'):
        cred = {
            'username': user,
            'password': password      
        }
        
        resp = requests.post(self.url + '/auth/login', json=cred)
        return resp.json()["userToken"]
    
    def create_new_employee(self, params):
        my_headers = {}        
        my_headers["x-client-token"] = self.get_token()
        
        my_params ={
            "id": fake.plate_number(),
            "firstName": fake.first_name_male(),
            "lastName": fake.last_name_male(), 
            "middleName": fake.middle_name_male(),
            "companyId": params["companyId"], 
            "email": fake.free_email(),
            "url": fake.hostname(),
            "phone": fake.msisdn(),
            "birthdate": str(fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80)),
            "isActive": params["isActive"]
        }
        
        resp = requests.post(self.url + '/employee', json=my_params, headers=my_headers)
        return resp.json()
        
    def get_company_employee(self, company_id):
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp.json()                     
    
    def get_employee(self, id_employee):
        resp = requests.get(self.url + '/employee/' + str(id_employee))
        return resp.json()
    
    def edit_employee(self, id_employee, params):
        my_headers = {}        
        my_headers["x-client-token"] = self.get_token()
        
        my_params ={
            "lastName": fake.last_name_male(), 
            "email": fake.free_email(),
            "url": fake.hostname(),
            "phone": fake.msisdn(),
            "isActive": params["isActive"]
        }
        
        resp = requests.patch(self.url + '/employee/' + str(id_employee), json=my_params, headers=my_headers)
        return resp.json()