is_year_leap = input("Введите високосный год: ")
is_year_leap = int(is_year_leap)

if (is_year_leap % 4 == 0):
    print(f"Да, {is_year_leap} этот год високосный ")
else:
    print(f"Ты ошибся, {is_year_leap} этот год не високосный")

