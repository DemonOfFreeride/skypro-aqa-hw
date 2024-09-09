import allure
from sqlalchemy import create_engine, inspect, text
from faker import Faker
fake = Faker('ru_RU')

class EmployeeTable:
    """
        Класс запросов в БД
    """     
    
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
    
    @allure.step("Получить список компаний (без помеченных на удаление)")
    def get_companies_without_deleted(self) -> list:
        """
            Функция получения спика компаний без помеченных на удаление
        """
        with self.__db.connect() as connection:
            query = connection.execute(self.__scripts["select_all_witout_delete_companies"])
            sql = str(query.context.compiled)   # Получаем и сразу преобразуем компилированный запрос в строку
            allure.attach(sql, 'SQL', allure.attachment_type.TEXT)   # Прикрепляем SQL-запрос к отчету Allure
            return query.fetchall()
       
    @allure.step("Получить список сотрудников компании")        
    def get_company_employee(self, company_id: int) -> list:
        """
            Функция получения спика сотрудников компании
        """        
        with self.__db.connect() as connection:
            query = connection.execute(self.__scripts["select_company_employee"], {'company_id': company_id})
            sql = str(query.context.compiled)
            allure.attach(sql, 'SQL', allure.attachment_type.TEXT)
            return query.fetchall()
    
    @allure.step("Получить данные одного сотрудника")    
    def get_employee(self, employee_id: int) -> dict:
        """
            Функция получения даннвх одного сотрудника
        """ 
        with self.__db.connect() as connection:
            query = connection.execute(self.__scripts["select_employee"], {'employee_id': employee_id})
            sql = str(query.context.compiled)
            allure.attach(sql, 'SQL', allure.attachment_type.TEXT)
            return query.fetchall()
  
    @allure.step("Ввести нового сотрудника")    
    def insert_new_employee(self, params) -> dict:
        """
            Функция ввода нового сотрудника
        """ 
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
            query = connection.execute(self.__scripts["insert_new_employee"], my_params)
            sql = str(query.context.compiled) 
            allure.attach(sql, 'SQL', allure.attachment_type.TEXT) 
            new_employee = query.fetchone()
            connection.commit()
            return new_employee

    @allure.step("Отредактировать данные сотрудника")
    def edit_employee(self, id_employee: int, params) -> dict:
        """
            Функция редактирования данных сотрудника
        """ 
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
            query =  connection.execute(self.__scripts["edit_employee"], my_params)
            sql = str(query.context.compiled)
            edited_employee = query.fetchone()
            connection.commit()
            return edited_employee
        
    @allure.step("Удалить сотрудника")   
    def delete_employee(self, id: int) -> dict:
        """
            Функция удаления сотрудника
        """
        with self.__db.connect() as connection:
            query = connection.execute(self.__scripts["delete_by_id"], {'id_to_delete': id})
            sql = str(query.context.compiled)
            allure.attach(sql, 'SQL', allure.attachment_type.TEXT)
            connection.commit()