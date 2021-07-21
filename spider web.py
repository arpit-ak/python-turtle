import turtle
t = turtle.Turtle()
s = turtle.Screen()

t.speed(0)
s.bgcolor('red')
t.pencolor('white')
t.pensize(5)
#Code for building radical thread
for i in range(6):
  t.pencolor('black')
  t.pensize(2)
  t.forward(200)
  t.backward(200)
  t.right(60)

#Code for building spiral thread
side = 200
for i in range(15):
  t.pensize(1)
  t.pencolor('black')
  t.penup()
  t.goto(0,0)
  t.pendown()

  t.setheading(0)
  t.pencolor('white')
  t.forward(side)
  t.right(120)
  for j in range(6):
    t.forward(side)
    t.right(60)
  side = side - 10
  t.hideturtle()
turtle.done()