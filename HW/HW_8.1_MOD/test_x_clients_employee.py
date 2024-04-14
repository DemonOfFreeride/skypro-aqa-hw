from faker import Faker
fake = Faker('ru_RU')
from time import sleep
from EmployeeApi import EmployeeApi


api = EmployeeApi("https://x-clients-be.onrender.com")

# - КАКИЕ МЕТОДЫ ПРОВЕРЯЕМ
# - [POST] /employee
# - [GET] /employee
# - [GET] /employee/{id}
# - [PATCH] /employee/{id}


def test_create_new_employee():
    api.create_new_data()   # создаем новые компании для теста
    sleep(3) # пацза для стабильной работы теста
    body_companies = api.get_company_list() 
    company_id = body_companies[0]["id"]   #  Записываем в переменную company_id первой компании из списка 
    body_company_employee = api.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
    
    new_employee = api.create_new_employee(params = {"companyId": company_id, "isActive": is_active})
    employee_id = new_employee["id"]
    assert employee_id != 0   # Проверка на создание нового сотрудника (для него создан "id")  
    body_company_employee = api.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
    
    assert body_company_employee[-1]["firstName"] == api.get_employee(employee_id)["firstName"]
    assert body_company_employee[-1]["lastName"] == api.get_employee(employee_id)["lastName"]
    assert body_company_employee[-1]["phone"] == api.get_employee(employee_id)["phone"]
    assert body_company_employee[-1]["email"] == api.get_employee(employee_id)["email"] # Бэк принимает данные, но фронт его (email) не выводит - Ошибка
    assert body_company_employee[-1]["companyId"] == company_id    


def test_get_employee_company():
    body_companies = api.get_company_list() 
    company_id = body_companies[1]["id"]   #  Записываем в переменную company_id второй компании из списка 
    body_company_employee = api.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
        
    new_employee = api.create_new_employee(params = {"companyId": company_id, "isActive": is_active})
    employee_id = new_employee["id"]
    assert employee_id != 0  # Проверка на создание нового сотрудника (для него создан "id")  
    body_company_employee = api.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
    
    assert body_company_employee[-1]["firstName"] == api.get_employee(employee_id)["firstName"]
    assert body_company_employee[-1]["lastName"] == api.get_employee(employee_id)["lastName"]
    assert body_company_employee[-1]["phone"] == api.get_employee(employee_id)["phone"]
    assert body_company_employee[-1]["companyId"] == company_id    
    
    
def test_get_employee():
    body_companies = api.get_company_list() 
    company_id = body_companies[2]["id"]    #  Записываем в переменную company_id третьей компании из списка
    body_company_employee = api.get_company_employee(company_id)
    len_before = len(body_company_employee)

    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
    
    new_employee = api.create_new_employee(params = {"companyId": company_id, "isActive": is_active})
    id_employee = new_employee["id"] 
    assert id_employee != 0  # Проверка на создание нового сотрудника (для него создан "id")
    body_company_employee = api.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
    
    body_emlpoyee = api.get_employee(id_employee)
    
    assert body_emlpoyee["firstName"] == api.get_company_employee(company_id)[-1]["firstName"]
    assert body_emlpoyee["lastName"] == api.get_company_employee(company_id)[-1]["lastName"]
    assert body_emlpoyee["companyId"] == company_id
    assert body_emlpoyee["birthdate"] == api.get_company_employee(company_id)[-1]["birthdate"]
    assert body_emlpoyee["phone"] == api.get_company_employee(company_id)[-1]["phone"]
    
    
def test_edit_employee():
    body_companies = api.get_company_list() 
    company_id = body_companies[3]["id"]    #  Записываем в переменную company_id четвертой компании из списка
    body_company_employee = api.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
    
    new_employee = api.create_new_employee(params = {"companyId": company_id, "isActive": is_active})   
    id_employee = new_employee["id"]
    assert id_employee != 0  # Проверка на создание нового сотрудника (для него создан "id")
    body_company_employee = api.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании

    edit_new_employee = api.edit_employee(id_employee, params = {"isActive": is_active})

    body_company_employee = api.get_company_employee(company_id)
    
    assert body_company_employee[-1]["lastName"] == api.get_employee(id_employee)["lastName"]
    assert body_company_employee[-1]["email"] == api.get_employee(id_employee)["email"]  # Только при редактировании фронт выдает email
    assert body_company_employee[-1]["avatar_url"] == api.get_employee(id_employee)["avatar_url"]
    assert body_company_employee[-1]["phone"] == api.get_employee(id_employee)["phone"]