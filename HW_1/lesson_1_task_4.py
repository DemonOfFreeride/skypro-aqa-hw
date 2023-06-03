first_name = input("First name: ")
last_name = input("Last name: ")
print("Your name is: " + first_name + " " + last_name)

# тоже самое только с применением f-строк в Python > 3.6 версиях

first_name = input("First name: ")
last_name = input("Last name: ")
print(f"Your name is: {first_name} + {last_name}")

# Можно вывести переменную и ее значение с помощью f-строки 

first_name = "Freddy"
last_name = "Mercury"
print(f"{first_name=} {last_name=}")