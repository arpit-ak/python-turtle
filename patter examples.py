import turtle
t=turtle.Turtle()
s=turtle.Screen()
list1=["yellow","red","blue","green"]
t.up()
t.goto(200,0)
for i in range(4):
    t.down()
    t.begin_fill()
    t.color(list1[i])
    t.pensize(20)
    t.circle(100)
    t.up()
    t.bk(100)
    
