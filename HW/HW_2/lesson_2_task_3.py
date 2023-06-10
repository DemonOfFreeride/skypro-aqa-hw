
import math  

def square(side):
        result = math.ceil(side ** 2)
        print(f"Площадь квадрата = {result}")

square(7)
square(2.3)

#    -- Через "IF"  используя оператор "TYPE"  --

import math  

def square(side):
    if type(side) == int or type(side) == float:
        result = math.ceil(side * side)
        print(f"Площадь квадрата = {result}")
    else: 
        print("Вы ввели не верные данные")

square(2)
square(3.3)
square("sdfsf")

#  --  еще один способ через "IF" используя оператор "TYPE"  -- 

import math 

def square(side):
    if type(side) in (int, float):
        result = math.ceil(side ** 2)
        print(f"Площадь квадрата = {result}")
    else:
        print("Вы ввели не верные данные")

square(4)
square(13.3)
square("JHfd")


#  -- способ через "IF" используя оператор "isinstance"  --

import math  

def square(side):
    if isinstance(side, (int, float)):
        result = math.ceil(side ** 2)
        print(f"Площадь квадрата = {result}")
    else:
        print("Вы ввели не верные данные")

square(5)
square(34.3)
square("sdgfh")