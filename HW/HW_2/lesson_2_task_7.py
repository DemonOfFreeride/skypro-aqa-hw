# 1. Создайте файл lesson_2_task_7.py.
# 2. Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# 3. Выведите сумму всех элементов списка.


# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# print(sum(lst))

# -- Та же задача но через циклы -- 

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

tot = 0

for i in lst: 
    tot += i

print(tot)    