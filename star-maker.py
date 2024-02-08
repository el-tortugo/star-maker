# Kehinde Adeoso
# kehinde.adeoso77@myhunter.cuny.edu
# Star-Maker

import turtle
t = turtle.Turtle()
wn = turtle.Screen()
x = -350
y = 300

n = input('How many stars? ')

bx, by = 350, 300

t.penup()
t.goto(x, y)

def position_check():
    global x, y
    if t.xcor() > bx:
        t.penup()
        y -= 110
        t.goto(x, y)
    t.pendown()


def create_star():
    position_check()
    t.speed(10)
    t.pendown()
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.penup()
    t.forward(150)
    

for i in range(int(n)):
    create_star()
    if i + 1 == 1:
        message = 'Star Created'
    else:
        message = 'Stars Created'
        
    print((i + 1), message)
t.hideturtle()
wn.exitonclick()