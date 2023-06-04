first_name = input("First name: ")
last_name = input("Last name: ")
print("Your name is: " + first_name + " " + last_name)

# https://medium.com/nuances-of-programming/простое-руководство-по-форматированию-строк-в-python-с-помощью-f-строк-ade71132102e#:~:text=F-строки%20—%20идеальный%20синтаксис%20для,следует%20еще%20добавить%20символ%20%7B%7D%20.
# тоже самое только с применением f-строк в Python > 3.6 версиях

first_name = input("First name: ")
last_name = input("Last name: ")
print(f"Your name is: {first_name} + {last_name}")

# Можно вывести переменную и ее значение с помощью f-строки 

first_name = "Freddy"
last_name = "Mercury"
print(f"{first_name=} {last_name=}")