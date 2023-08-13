#  ===================  ЗАДАНИЕ 1 ===================

# 1. Создайте файл `user.py`.
# 2. В файле объявите класс `User`.
# 3. Объявите в классе конструктор.

# Конструктор должен принимать на вход 2 параметра:

# 1. `first_name` — имя.
# 2. `last_name` — фамилия.

# Помните, что все методы класса, включая конструктор, принимают первым параметром `self`.

# 4. Создайте в классе 3 метода, которые печатают:
#     - имя,
#     - фамилию,
#     - имя и фамилию.
# 5. Создайте файл `lesson_3_task_1.py`.
# 6. Импортируйте в него класс `user`.
# 7. Создайте новый экземпляр `User` и сохраните его в переменную `my_user`.
# 8. Вызовите все методы у объекта в переменной `my_user`.


from user import User

my_user = User("Tim", "Hunt")

my_user.seyF_name()
my_user.sayL_name()
my_user.sayFL_name()