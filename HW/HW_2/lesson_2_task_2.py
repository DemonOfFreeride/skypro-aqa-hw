# 1. Создайте файл lesson_2_task_2.py.
# 2. Создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, если год високосный, и False — иначе.
# 3. В этом же файле напишите код, который вызывает функцию и передает в нее год (выберите любой).
# 4. Результат вызова функции должен сохраняться в переменную.
# 5. Выведите в консоль ответ: `год <номер года>: <True|False>`


# is_year_leap = int(input("Введите високосный год: "))

# if (is_year_leap % 4 == 0):
#     print(f"Да, {is_year_leap} этот год високосный ")
# else:
#     print(f"Ты ошибся, {is_year_leap} этот год не високосный")



#  --  С проверкой на ввод целого числа через функцию try --

# def is_year_leap(year):
#     try:
#         int_year = int(year)
#     except ValueError:
#         print("Вы ввели не целое число")
#         return False
#     if (int_year % 4 == 0):
#         print(f"Да, {int_year} этот год високосный ")
#     else:
#         print(f"Ты ошибся, {int_year} этот год не високосный")
    
# year = input("Введите високосный год: ")

# is_year_leap(year)


#  --  С повторением цикла while пока не введем целоле число  --

def is_year_leap(year):
    while True:
        try:
            int_year = int(year)
            if (int_year % 4 == 0):
                print(f"Да, {int_year} этот год високосный ")
            else:
                print(f"Ты ошибся, {int_year} этот год не високосный")
            break
        except ValueError:
            print("Вы ввели не целое число")
            year = input("Введите високосный год: ")
                        
year = input("Введите високосный год: ")

is_year_leap(year)            