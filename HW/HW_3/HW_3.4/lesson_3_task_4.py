#     ================  ЗАДАНИЕ 4 ===============

# 2. Скопируйте и запустите код:
    
#     ```python
#     from turtle import *
    
#     my_turtle = Turtle()
#     my_turtle.speed(0)
#     my_turtle.screen.setup(1200, 800)
    
#     # Нарисовать квадрат
#     def draw_rect(t):
#         for x in range(0, 4):
#             t.right(90)
#             t.forward(100)
    
#     # Рисует квадраты в цикле
#     for x in range(0, 360):
#         draw_rect(my_turtle)
#         my_turtle.right(1)
    
#     # Необходимо, чтобы окно не закрывалось само, а только по клику
#     my_turtle.screen.exitonclick()
#     my_turtle.screen.mainloop()
    
#     ```
    
# 3. Изучите структуру кода  на предмет основных блоков.
# 4. Изучите статьи:
# - «**Графика turtle черепашка в питон»:**  http://itrobo.ru/programmirovanie/python/grafika-turtle-cherepashka-v-piton.html
# - «****Черепаха (turtle) в python»:**** https://koddom.com/kodim/turtle-python/****.****
# 1. Напишите код, который рисует изображение любого животного.
# 2. Поделитесь скриншотом рисунка в чате с коллегами.


from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(800, 600)

my_turtle.fillcolor("gray")
my_turtle.begin_fill()
my_turtle.circle(50)
my_turtle.end_fill()

my_turtle.fillcolor("gray")
my_turtle.begin_fill()
my_turtle.penup()
my_turtle.goto(-0, 80)
my_turtle.pendown()
my_turtle.circle(30)
my_turtle.end_fill()

my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.penup()
my_turtle.goto(-45, 110)
my_turtle.pendown()
my_turtle.goto(-15, 110)
my_turtle.goto(-30, 145)
my_turtle.goto(-45, 110)
my_turtle.end_fill()

my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.penup()
my_turtle.goto(15, 110)
my_turtle.pendown()
my_turtle.goto(45, 110)
my_turtle.goto(30, 145)
my_turtle.goto(15, 110)
my_turtle.end_fill()

my_turtle.fillcolor("white")
my_turtle.begin_fill()
my_turtle.penup()
my_turtle.goto(-20, 100)
my_turtle.pendown()
my_turtle.circle(10)
my_turtle.end_fill()

my_turtle.fillcolor("white")
my_turtle.begin_fill()
my_turtle.penup()
my_turtle.goto(20, 100)
my_turtle.pendown()
my_turtle.circle(10)
my_turtle.end_fill()

my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.penup()
my_turtle.goto(-20, 100)
my_turtle.pendown()
my_turtle.circle(5)
my_turtle.end_fill()

my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.penup()
my_turtle.goto(20, 100)
my_turtle.pendown()
my_turtle.circle(5)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(-1, 95)
my_turtle.pendown()
my_turtle.circle(5)

my_turtle.penup()
my_turtle.goto(-6, 90)
my_turtle.pendown()
my_turtle.forward(20)


my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()

