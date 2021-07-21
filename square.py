import turtle
a=turtle.Turtle()
a.color("white")
b=turtle.Screen()
b.bgcolor("black")
a.speed(0)
a.begin_fill()
a.fillcolor("red")
for i in range(4):
    a.forward(100)
    a.left(90)
a.end_fill()
a.hideturtle()    
    
