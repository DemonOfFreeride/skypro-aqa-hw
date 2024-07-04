from sqlalchemy import create_engine, inspect, text
from faker import Faker
fake = Faker('ru_RU')

class EmployeeTable:
    
    __scripts = {
        "select_company_employee": text("SELECT * FROM employee where \"company_id\" = :company_id ORDER BY \"id\" ASC"), # отдает данные с сортировкой по id (как в методе API)
        "select_employee": text("SELECT * FROM employee where \"id\" = :employee_id"),
        "select_all_witout_delete_companies": text('SELECT * FROM company where \"deleted_at\" is NULL'),
        "insert_new_employee": text("""
            INSERT INTO employee("id", "first_name", "last_name", "middle_name", "company_id", "email", "avatar_url", "phone", "birthdate", "is_active") 
            values (:id, :firstName, :lastName, :middleName, :companyId, :email, :avatar_url, :phone, :birthdate, :isActive)
            RETURNING *
            """),       
        "edit_employee": text("""
            UPDATE employee
            SET "first_name" = :firstName, 
                "last_name" = :lastName, 
                "email" = :email,
                "avatar_url" = :avatar_url, 
                "phone" = :phone,
                "is_active" = :isActive 
            WHERE "id" = :id_employee
            RETURNING *
            """),
        "delete_by_id": text("delete from employee where id = :id_to_delete")
    }
    
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
    
    def get_companies_without_deleted(self):
        with self.__db.connect() as connection:
            return [dict(row._mapping) for row in connection.execute(self.__scripts["select_all_witout_delete_companies"]).fetchall()]
            
    def get_company_employee(self, company_id):
        with self.__db.connect() as connection:
            return connection.execute(self.__scripts["select_company_employee"], {'company_id': company_id}).fetchall() # У скрипта 
        
    def get_employee(self, employee_id):
        with self.__db.connect() as connection:
            return connection.execute(self.__scripts["select_employee"], {'employee_id': employee_id}).fetchall()   
        
    def insert_new_employee(self, params):
        with self.__db.connect() as connection:
            my_params ={
                "id": fake.plate_number(),
                "firstName": fake.first_name_male(),
                "lastName": fake.last_name_male(), 
                "middleName": fake.middle_name_male(),
                "companyId": params["companyId"], 
                "email": fake.free_email(),
                "avatar_url": fake.hostname(),
                "phone": fake.msisdn(),
                "birthdate": str(fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80)),
                "isActive": params["isActive"]
            }
            result =  connection.execute(self.__scripts["insert_new_employee"], my_params)
            new_employee = result.fetchone()
            connection.commit()
            return new_employee
            
    def edit_employee(self, id_employee, params):
        with self.__db.connect() as connection:
            my_params ={
                "id_employee": id_employee,
                "firstName": fake.first_name_male(),
                "lastName": fake.last_name_male(),
                "email": fake.free_email(),
                "avatar_url": fake.hostname(),
                "phone": fake.msisdn(),
                "isActive": params["isActive"]
            }
            result =  connection.execute(self.__scripts["edit_employee"], my_params)
            edited_employee = result.fetchone()
            connection.commit()
            return edited_employee
        
    def delete_employee(self, id):
        with self.__db.connect() as connection:
            connection.execute(self.__scripts["delete_by_id"], {'id_to_delete': id})
            connection.commit()