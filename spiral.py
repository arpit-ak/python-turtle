import turtle
t = turtle.Turtle()
s = turtle.Screen()
turtle.color(0,0,255)
t.speed(0)
s.bgcolor('black')
r,g,b=255,0,0
for i in range(255*2):
  
  if i<255//3:
    g+=3
  elif i<255*2//3:
    r-=3
  elif i<255:
    b+=3
  elif i<255*4//3:
    g-=3
  elif i<255*5//3:
    r+=3
  else:
    b-=3
  t.forward(7+i)
  t.right(91)
  t.pencolor(r,g,b)  
t.hideturtle()
turtle.done()