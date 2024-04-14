from TodoListApi import TodoListApi


api = TodoListApi('https://todo-app-sky.herokuapp.com/')


def test_create_new_task():
    todo_list = api.get_list_todo()
    len_before = len(todo_list) 
    print(len_before)
    
    completed = False
    
    result = api.create_new_task(params = {"completed": completed})
    id_task = result["id"]
    
    assert result["id"] != 0 # Проверка на создание новой задачи (для нее создан "id")
    
    todo_list = api.get_list_todo()
    len_after = len(todo_list)
    assert len_after - len_before == 1  # Проверка на добавление новой задачи
    
    api.delete_task(id_task) # Удаляем после себя задачу
    
    
def test_get_task():

    completed = False
    
    new_task = api.create_new_task(params = {"completed": completed})
    id_task = new_task["id"]
    
    result = api.get_task(id_task)
    
    assert result["id"] == id_task  # Проверка на соответсвие id задачи 
    assert result["title"] == new_task["title"]  # Проверка на сооответсвие описания задачи 
    
    api.delete_task(id_task) # Удаляем после себя задачу
    

def test_reduct_task():
    
    completed = False
    
    new_task = api.create_new_task(params = {"completed": completed})
    id_task = new_task["id"]
    title_task = new_task["title"]
    
    result = api.reduct_task(id_task, params = {"completed": completed})
    
    assert result["id"] == id_task  # Проверка на соответсвие id задачи 
    assert result["title"] != title_task  # Проверка на не сооответсвие описания задачи до и после редактирования 
    assert result["title"] == api.get_task(id_task)["title"] # Проверка на сооответсвие описания задачи после редактирования
    
    api.delete_task(id_task) # Удаляем после себя задачу

    
def test_delete_task():
    
    completed = False
    
    new_task = api.create_new_task(params = {"completed": completed})
    id_task = new_task["id"]
    
    assert new_task["id"] != 0  # Проверка на создание новой задачи (для нее создан "id")
    
    result = api.delete_task(id_task)
    
    all_tasks = api.get_list_todo()
    
    for task in all_tasks:   # Проверка на отсутвие в элементе списка созданого ранее id (удаленной) задачи
        assert task["id"] != id_task    
           
           
def test_change_status():
    
    completed = False
    
    new_task = api.create_new_task(params = {"completed": completed})
    id_task = new_task["id"]
    
    assert new_task["id"] != 0  # Проверка на создание новой задачи (для нее создан "id")
    assert new_task["completed"] == False  # Проверка на НЕ завершенность задачи 
    
    completed = True
    
    status_done = api.change_status_task(id_task, params = {"completed": completed})
    
    assert status_done["completed"] == True  # Проверка на завершенность задачи
    
    completed = False

    cancel_stat_done = api.change_status_task(id_task, params = {"completed": completed})
    
    assert cancel_stat_done["completed"] == False  # Проверка на НЕ завершенность задачи 
    
    api.delete_task(id_task) # Удаляем после себя задачу