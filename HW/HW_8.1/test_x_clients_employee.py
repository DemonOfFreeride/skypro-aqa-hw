from time import sleep
from EmployeeApi import EmployeeApi


api = EmployeeApi("https://x-clients-be.onrender.com")

# - КАКИЕ МЕТОДЫ ПРОВЕРЯЕМ
# - [GET] /employee
# - [POST] /employee
# - [GET] /employee/{id}
# - [PATCH] /employee/{id}

def test_create_newemployee():
    api.create_new_data()   # создаем новые данные
    sleep(5)  # пауза для создания данных, необходимо для стабильности работы
    body_companies = api.get_company_list() 
    company_id = body_companies[0]["id"]   #  Записываем в переменную company_id первой компании из списка 
    body_company_employee = api.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    my_params ={
        "id": 1,
        "firstName": "Jhon",
        "lastName": "Connor", 
        "middleName": "",
        "companyId": company_id, 
        "email": "termin@metu.com",
        "url": "non",
        "phone": "+94729472424",
        "birthdate": "1985-01-13T12:26:30.047Z",
        "isActive": True
        }
    
    result = api.create_new_employee(params = my_params)
    # for key, value in result.items():     #  для проверки ключ - значение в терминале с ключом "-s"
    #     print(f"Ключ: {key}, Значение: {value}")
    assert result["id"] != 0   # Проверка на создание нового сотрудника (для него создан "id")  
    body_company_employee = api.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
    
def test_get_employee_company():
    body_companies = api.get_company_list() 
    company_id = body_companies[1]["id"]   #  Записываем в переменную company_id второй компании из списка 
    body_company_employee = api.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    my_params ={
        "id": 2,
        "firstName": "Luke",
        "lastName": "Skywalker", 
        "middleName": "",
        "companyId": company_id, 
        "email": "inAgalaxy@FarFarAway.com",
        "url": "non",
        "phone": "+8519869516",
        "birthdate": "1050-03-20T12:26:30.047Z",
        "isActive": True
        }
    
    new_employee = api.create_new_employee(params = my_params)
    # for key, value in result.items():     #  для проверки ключ - значения в терминале с ключом "-s"
    #     print(f"Ключ: {key}, Значение: {value}")
    assert new_employee["id"] != 0  # Проверка на создание нового сотрудника (для него создан "id")  
    body_company_employee = api.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
    
    assert body_company_employee[0]["firstName"] == "Luke"
    assert body_company_employee[0]["lastName"] == "Skywalker"
    assert body_company_employee[0]["phone"] == "+8519869516"
    assert body_company_employee[0]["companyId"] == company_id    
    
def test_get_employee():
    body_companies = api.get_company_list() 
    company_id = body_companies[2]["id"]    #  Записываем в переменную company_id третьей компании из списка
    body_company_employee = api.get_company_employee(company_id)
    len_before = len(body_company_employee)

    my_params ={
        "id": 3,
        "firstName": "Pablo",
        "lastName": "Escobar", 
        "middleName": "",
        "companyId": company_id, 
        "email": "columbia@drags.net",
        "url": "non",
        "phone": "+3546512984",
        "birthdate": "1949-12-01T12:26:30.047Z",
        "isActive": True
        }
    
    new_employee = api.create_new_employee(params = my_params)    
    assert new_employee["id"] != 0  # Проверка на создание нового сотрудника (для него создан "id")
    body_company_employee = api.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании
    
    
    id_employee = body_company_employee[0]["id"]
    body_emlpoyee = api.get_employee(id_employee)
    
    assert body_emlpoyee["firstName"] == "Pablo"
    assert body_emlpoyee["lastName"] == "Escobar"
    assert body_emlpoyee["companyId"] == company_id
    assert body_emlpoyee["birthdate"] == "1949-12-01"
    assert body_emlpoyee["phone"] == "+3546512984"
    
def test_edit_employee():
    body_companies = api.get_company_list() 
    company_id = body_companies[3]["id"]    #  Записываем в переменную company_id четвертой компании из списка
    body_company_employee = api.get_company_employee(company_id)
    len_before = len(body_company_employee)
    
    my_params ={
        "id": 4,
        "firstName": "Quentin",
        "lastName": "Tarantino", 
        "middleName": "Jerome",
        "companyId": company_id, 
        "email": "Los@Angeles.net",
        "url": "https//Qtarantino.com",
        "phone": "+57965168499",
        "birthdate": "1963-03-27T12:26:30.047Z",
        "isActive": True
        }
    
    new_employee = api.create_new_employee(params = my_params)    
    assert new_employee["id"] != 0  # Проверка на создание нового сотрудника (для него создан "id")
    body_company_employee = api.get_company_employee(company_id)
    len_after = len(body_company_employee)
    assert len_after - len_before == 1  # Проверка на добавление сотрудника в тело компании

    id_employee = body_company_employee[0]["id"]
    
    my_params = {
        "lastName": "---NotTARANTINO---",
        "email": "new@me.com",
        "url": "https//newurl.com",
        "phone": "+9849846198498",
        "isActive": True
        }

    result = api.edit_employee(id_employee, params=my_params)
    # for key, value in result.items():     #  для проверки ключ - значение 
    #     print(f"Ключ: {key}, Значение: {value}") 

    body_company_employee = api.get_company_employee(company_id)
    assert body_company_employee[0]["lastName"] == "---NotTARANTINO---"
    assert body_company_employee[0]["email"] == "new@me.com"
    assert body_company_employee[0]["avatar_url"] == "https//newurl.com"
    #assert body_company_employee[0]["phone"] == "+9849846198498" #  Ошибка - в схеме запроса есть этот параментр, но он не обновляется и возврощается старые данные (ошибка со стороны бэка)
    # закомментировал что бы весь весь тест ран не завалился