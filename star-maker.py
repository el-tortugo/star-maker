# Kehinde Adeoso
# kehinde.adeoso77@myhunter.cuny.edu
# Star-Maker

import turtle
t = turtle.Turtle()
x = -350
y = 300

bx, by = 350, 300

t.penup()
t.goto(x, y)

def position_check(x, y):
    if t.xcor() > bx:
        t.penup()
        y -= 110
        t.goto(x, y)
    t.pendown()


def create_star(x, y):
    position_check(x, y)
    t.speed(10)
    t.pendown()
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.penup()
    t.forward(150)
    

for i in range(12):
    create_star(x, y)
    if i + 1 == 1:
        message = 'Star Created'
    else:
        message = 'Stars Created'
        
    print((i + 1), message)
t.hideturtle()
input("Mission Complete! Click here and press ENTER ") # keeps turtles from closing prematurely



