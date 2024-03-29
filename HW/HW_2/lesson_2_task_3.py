# 1. Создайте файл lesson_2_task_3.py.
# 2. Напишите функцию square, принимающую 1 аргумент — сторону квадрата — и возвращающую площадь квадрата.
# 3. Если переданный аргумент был не целым, округлите результат вверх.


# import math  

# def square(side):
#         result = math.ceil(side ** 2)
#         print(f"Площадь квадрата = {result}")

# square(7)
# square(2.3)

# #    -- Через "IF"  используя оператор "TYPE"  --

# import math  

# def square(side):
#     if type(side) == int or type(side) == float:
#         result = math.ceil(side * side)
#         print(f"Площадь квадрата = {result}")
#     else: 
#         print("Вы ввели не верные данные")

# square(2)
# square(3.3)
# square("sdfsf")

# #  --  еще один способ через "IF" используя оператор "TYPE"  -- 

# import math 

# def square(side):
#     if type(side) in (int, float):
#         result = math.ceil(side ** 2)
#         print(f"Площадь квадрата = {result}")
#     else:
#         print("Вы ввели не верные данные")

# square(4)
# square(13.3)
# square("JHfd")


#  -- способ через "IF" используя оператор "isinstance"  --

# import math  

# def square(side):
#     if isinstance(side, (int, float)):
#         result = math.ceil(side ** 2)
#         print(f"Площадь квадрата = {result}")
#     else:
#         print("Вы ввели не верные данные")

# side = int or float(input("Введите длину стороны квадрата: "))


# square(5)
# square(34.3)
# square("sdgfh")

# -- способ с "try" и "except" ввод значения с консоли, проврка на корректность данных при вводе -- 

import math

def square(side):
    try:
        side = int(side)
        if side > 0:
            area = side ** 2
            print("Площадь квадрата:", area)
            return True
        else:
            print("Вы ввели неположительное число, попробуйте еще раз")
            return False
    except ValueError:
        try:
            side = float(side)
            if side > 0:
                area = math.ceil(side ** 2)
                print("Площадь квадрата:", area)
                return True
            else:
                print("Вы ввели не положительное число, попробуйте еще раз")
                return False
        except ValueError:
            print("Вы ввели неверные данные, попробуйте еще раз")
            return False


while True:
    side = input("Введите сторону квадрата: ")
    if square(side):
        break
