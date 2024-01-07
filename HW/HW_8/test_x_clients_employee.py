from EmployeeApi import EmployeeApi

api = EmployeeApi("https://x-clients-be.onrender.com")

def test_get_employees_companies():
    body = api.get_company_employee(3219)
    return body