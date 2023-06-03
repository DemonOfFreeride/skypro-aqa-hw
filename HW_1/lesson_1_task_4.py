first_name = input("First name: ")
last_name = input("Last name: ")
print("Your name is: " + first_name + " " + last_name)

# https://medium.com/nuances-of-programming/%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5-%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E-%D1%81%D1%82%D1%80%D0%BE%D0%BA-%D0%B2-python-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-f-%D1%81%D1%82%D1%80%D0%BE%D0%BA-ade71132102e#:~:text=F-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8%20%E2%80%94%20%D0%B8%D0%B4%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%81%20%D0%B4%D0%BB%D1%8F,%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D0%B5%D1%82%20%D0%B5%D1%89%D0%B5%20%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%20%7B%7D%20.
# тоже самое только с применением f-строк в Python > 3.6 версиях

first_name = input("First name: ")
last_name = input("Last name: ")
print(f"Your name is: {first_name} + {last_name}")

# Можно вывести переменную и ее значение с помощью f-строки 

first_name = "Freddy"
last_name = "Mercury"
print(f"{first_name=} {last_name=}")