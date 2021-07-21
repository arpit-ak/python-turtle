Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> debo=turtle.Turtle()
>>> kibo=turtle.Screen()
>>> kibo.pencolor("red")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    kibo.pencolor("red")
AttributeError: '_Screen' object has no attribute 'pencolor'
>>> debo.pencolor("red")
>>> debo.pencolor("black")
>>> kibo.forward(100)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    kibo.forward(100)
AttributeError: '_Screen' object has no attribute 'forward'
>>> debo.forward(100)
>>> debo.left(90)
>>> debo.forward(100)
>>> debo.left(90)
>>> debo.forward(100)
>>> debo.left(90)
>>> debo.forward(100)
>>> 