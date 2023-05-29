def tel_Sky(num):
    return str(num)

result = tel_Sky(8) + tel_Sky(8) + tel_Sky(0) + tel_Sky(0) + tel_Sky(5) + tel_Sky(5) + tel_Sky(5) + tel_Sky(3) + tel_Sky(5) + tel_Sky(3) + tel_Sky(5)
print(result)   #  - на практике вызывать множество функций в одну строку - плохой вариант (из-за плохой читаемости)

# -  Другой способ не в строчку

def tel_Sky2(num):
    print(num)

tel_Sky2(8)
tel_Sky2(8)
tel_Sky2(0)
tel_Sky2(0)
tel_Sky2(5)
tel_Sky2(5)
tel_Sky2(5)
tel_Sky2(3)
tel_Sky2(5)
tel_Sky2(3)
tel_Sky2(5)