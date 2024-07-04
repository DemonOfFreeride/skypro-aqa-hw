from time import sleep
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable ("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

def test_create_new_employee():
    body_companies = db.get_companies_without_deleted()
    company_id = body_companies[0]["id"]   #  Записываем в переменную company_id первой компании из списка (не обязательно это число максимальное)
    body_company_employee = db.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
    
    new_employee = db.insert_new_employee(params = {"companyId": company_id, "isActive": is_active})
    id_new_employee = new_employee[0]

    assert id_new_employee != 0   # Проверка на создание нового сотрудника (для него создан "id")  
    body_company_employee = db.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
    
    assert new_employee[4] == api.get_employee(id_new_employee)["firstName"]
    assert new_employee[5] == api.get_employee(id_new_employee)["lastName"]
    assert new_employee[6] == api.get_employee(id_new_employee)["middleName"]
    assert new_employee[7] == api.get_employee(id_new_employee)["phone"]
    assert new_employee[8] == api.get_employee(id_new_employee)["email"] 
    assert new_employee[9].strftime('%Y-%m-%d') == api.get_employee(id_new_employee)["birthdate"]  # возврат иб БД маски отображания даты как в API  
    assert new_employee[10] == api.get_employee(id_new_employee)["avatar_url"]
    assert new_employee[11] == api.get_employee(id_new_employee)["companyId"]
    
    db.delete_employee(id_new_employee) 
 
def test_get_company_employee():
    body_companies = db.get_companies_without_deleted()
    company_id = body_companies[1]["id"]   #  Записываем в переменную company_id второй компании из списка 
    body_company_employee = db.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
        
    new_employee = db.insert_new_employee(params = {"companyId": company_id, "isActive": is_active})
    id_new_employee = new_employee[0]
    assert id_new_employee != 0  # Проверка на создание нового сотрудника (для него создан "id")  
    body_company_employee = db.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
  
    assert body_company_employee[-1][4] == api.get_company_employee(company_id)[-1]["firstName"]
    assert body_company_employee[-1][5] == api.get_company_employee(company_id)[-1]["lastName"]
    assert body_company_employee[-1][7] == api.get_company_employee(company_id)[-1]["phone"]
    assert body_company_employee[-1][11] == api.get_company_employee(company_id)[-1]["companyId"]
    
    db.delete_employee(id_new_employee) 
 
def test_get_employee():
    body_companies = db.get_companies_without_deleted()
    company_id = body_companies[2]["id"]    #  Записываем в переменную company_id третьей компании из списка
    body_company_employee = db.get_company_employee(company_id)
    len_before = len(body_company_employee)

    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
    
    new_employee = db.insert_new_employee(params = {"companyId": company_id, "isActive": is_active})
    id_new_employee = new_employee[0]
    assert id_new_employee != 0  # Проверка на создание нового сотрудника (для него создан "id")
    body_company_employee = db.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании

    assert db.get_employee(id_new_employee)[0][4] == api.get_employee(id_new_employee)["firstName"]
    assert db.get_employee(id_new_employee)[0][5] == api.get_employee(id_new_employee)["lastName"]
    assert db.get_employee(id_new_employee)[0][11] == api.get_employee(id_new_employee)["companyId"]
    assert db.get_employee(id_new_employee)[0][9].strftime('%Y-%m-%d') == api.get_employee(id_new_employee)["birthdate"] # возврат иб БД маски отображания даты как в API
    assert db.get_employee(id_new_employee)[0][7] == api.get_employee(id_new_employee)["phone"] 
    
    db.delete_employee(id_new_employee) 

def test_edit_employee():
    body_companies = db.get_companies_without_deleted()
    company_id = body_companies[3]["id"]    #  Записываем в переменную company_id четвертой компании из списка
    body_company_employee = db.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
    
    new_employee = db.insert_new_employee(params = {"companyId": company_id, "isActive": is_active}) 
    id_new_employee = new_employee[0]
    assert id_new_employee != 0  # Проверка на создание нового сотрудника (для него создан "id")
    body_company_employee = db.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
    
    edited_new_employee = db.edit_employee(id_new_employee, params = {"isActive": is_active})
    
    assert edited_new_employee[4] == api.get_employee(id_new_employee)["firstName"]
    assert edited_new_employee[5] == api.get_employee(id_new_employee)["lastName"]
    assert edited_new_employee[8] == api.get_employee(id_new_employee)["email"] 
    assert edited_new_employee[10] == api.get_employee(id_new_employee)["avatar_url"]
    assert edited_new_employee[7] == api.get_employee(id_new_employee)["phone"]
    
    db.delete_employee(id_new_employee)
    
def test_delete_employee():
    body_companies = db.get_companies_without_deleted()
    company_id = body_companies[4]["id"]    #  Записываем в переменную company_id пятой компании из списка
    body_company_employee = db.get_company_employee(company_id)
    len_before_delete = len(body_company_employee)
    
    is_active = True #  Переменная для смены статуса сотрудника, по умолчанию "True"
    
    new_employee = db.insert_new_employee(params = {"companyId": company_id, "isActive": is_active}) 
    id_new_employee = new_employee[0]
    
    db.delete_employee(id_new_employee)
    body_company_employee = db.get_company_employee(company_id)
    len_after_delete = len(body_company_employee)
    assert len_after_delete == len_before_delete # Проверка на длину списка, равна изначальному до добавления нового сотрудника
    
    company_employees = api.get_company_employee(company_id)
    employee_ids = [employee['id'] for employee in company_employees]  # создаем список из всех id клиентов компании
    assert id_new_employee not in employee_ids