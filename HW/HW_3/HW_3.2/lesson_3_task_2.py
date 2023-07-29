#     ================  ЗАДАНИЕ 2 ===============

# 1. Создайте файл `smartphone.py`.
# 2. В файле объявите класс `Smartphone`.
# 3. Объявите в классе конструктор.

# Конструктор должен принимать на вход следующие параметры:

# - марка телефона,
# - модель телефона,
# - абонентский номер (”+79…”).
# 4. Создайте файл `lesson_3_task_2.py`.
# 5. В файле объявите переменную `catalog`.
# 6. Переменная хранит в себе список (`[]`).
# 7. Наполните список пятью разными экземплярами класса `Smartphone`.
# 8. Напишите цикл, который печатает весь каталог (список) в формате `<марка> - <модель>. <номер телефона>`.


from smartphone import Smartphone

cat_all_1 = Smartphone("samsung", "galaxy S8" , "+79161234567")
cat_all_2 = Smartphone("nokia", "610" , "+79161234568")
cat_all_3 = Smartphone("apple", "iphone 12" , "+79161234569")
cat_all_4 = Smartphone("blackberry", "curve" , "+79161234570")
cat_all_5 = Smartphone("htc", "desire" , "+79161234571")

catalog = [cat_all_1, cat_all_2, cat_all_3, cat_all_4, cat_all_5]

for phone in catalog:
    phone.cat_all()



# -- способ добавдения в список через функцию append --  

catalog = []
catalog.append(Smartphone("samsung", "galaxy a20", "+79161234567"))
catalog.append(Smartphone("apple", "iphone 12", "+79162345678"))
catalog.append(Smartphone("xiaomi", "mi 11", "+79163456789"))
catalog.append(Smartphone("huawei", "p40 pro", "+79164567890"))
catalog.append(Smartphone("oneplus", "9 pro", "+79165678901"))

for phone in catalog:
    print(phone.brand, "-", phone.model + ".", phone.number)        