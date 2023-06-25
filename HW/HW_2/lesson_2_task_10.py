def bank(x, y):
    for i in range(y):
        x += int(x * 0.1)
    res = x
    print(f'Ваше счет через {y} лет будет {res}')

x = int(input("Сколько денег хотите вложить: "))
y = int(input("На сколько лет? "))

bank(x , y)