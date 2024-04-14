import requests
from faker import Faker
fake = Faker('ru_RU')


class TodoListApi:
    
    def __init__(self, url):
        self.url = url
        
    def get_list_todo(self):
        resp = requests.get(self.url)
        return resp.json()
        
    def create_new_task(self, params):
        
        my_params ={
            "title": fake.catch_phrase(),
            "completed": params["completed"]
        }
        
        resp = requests.post(self.url, json=my_params)
        return resp.json()
    
    def get_task(self, id_task):
        resp = requests.get(self.url + str(id_task))
        return resp.json()
    
    def reduct_task(self, id_task, params):
        
        my_params ={
            "title": fake.catch_phrase(),
            "completed": params["completed"]
        }        
        
        resp = requests.patch(self.url + str(id_task), json=my_params)
        return resp.json()
    
    def delete_task(self, id_task):
        resp = requests.delete(self.url + str(id_task))
        # return resp.json()
    
    def change_status_task(self, id_task, params):
        resp = requests.patch(self.url + str(id_task), json=params)
        return resp.json()