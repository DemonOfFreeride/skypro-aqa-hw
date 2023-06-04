def a():
    print(1)
    return "1"
def b():
    return "2"
def c():
    return "3"
def d():
    return "4"
def e():
    return "5"
def f():
    return "6"
def g():
    return "7"
def h():
    return "8"
def i():
    return "9"
def j():
    return "0"

result = h() + h() + j() + j() + e() + e() + e() + c() + e() + c() + e()
print(result)

#  -  Другой способ не в строчку

def aa():
    print(1)
def bb():
    print(2)
def cc():
    print(3)
def dd():
    print(4)
def ee():
    print(5)
def ff():
    print(6)
def gg():
    print(7)
def hh():
    print(8)
def ii():
    print(9)
def jj():
    print(0)

hh() 
hh()
jj()
jj()
ee()
ee()
ee()
cc()
ee()
cc()
ee()

#  - https://dev-gang.ru/article/python-funkcija-print-i-parametr-end-uxnl9natxr/
#  - Использование параметра end в print() 

def aa():
    print(1, end = ' ')
def bb():
    print(2, end = ' ')
def cc():
    print(3, end = ' ')
def dd():
    print(4, end = ' ')
def ee():
    print(5, end = ' ')
def ff():
    print(6, end = ' ')
def gg():
    print(7, end = ' ')
def hh():
    print(8, end = ' ')
def ii():
    print(9, end = ' ')
def jj():
    print(0, end = ' ')

hh() 
hh()
jj()
jj()
ee()
ee()
ee()
cc()
ee()
cc()
ee()