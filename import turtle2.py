import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('blue')
t.speed(0)
for i in range(6):
    for color in ('red','magenta','cyan','green','white','yellow',):
        t.color(color)
        t.circle(100)
        t.left(10)

t.hideturtle()
turtle.done()