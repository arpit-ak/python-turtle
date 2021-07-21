Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> debo=turtle.Turtle()
>>> kibo=turtle.Screen()
>>> kibo.bgcolor("red")
>>> kibo.bgcolor("white")
>>> debo.setheading(90)
>>> t.setheading(180)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t.setheading(180)
NameError: name 't' is not defined
>>> debo.setheading(180)
>>> debo.setheading(270)
>>> debo.setheading(360)
>>> deo.forward(100)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    deo.forward(100)
NameError: name 'deo' is not defined
>>> debo.forward(100)
>>> debo.forward(50)
>>> debo.fd(10)
>>> help.(turtle.forward)
SyntaxError: invalid syntax
>>> help(turtle.forward)
Help on function forward in module turtle:

forward(distance)
    Move the turtle forward by the specified distance.
    
    Aliases: forward | fd
    
    Argument:
    distance -- a number (integer or float)
    
    Move the turtle forward by the specified distance, in the direction
    the turtle is headed.
    
    Example:
    >>> position()
    (0.00, 0.00)
    >>> forward(25)
    >>> position()
    (25.00,0.00)
    >>> forward(-75)
    >>> position()
    (-50.00,0.00)

>>> debo.fd(-300)
>>> help(turtle.backward)
Help on function backward in module turtle:

backward(distance)
    Move the turtle backward by distance.
    
    Aliases: back | backward | bk
    
    Argument:
    distance -- a number
    
    Move the turtle backward by distance ,opposite to the direction the
    turtle is headed. Do not change the turtle's heading.
    
    Example:
    >>> position()
    (0.00, 0.00)
    >>> backward(30)
    >>> position()
    (-30.00, 0.00)

>>> debo.bk(10)
>>> debo.bk(-100)
>>> help(turtle.left)
Help on function left in module turtle:

left(angle)
    Turn turtle left by angle units.
    
    Aliases: left | lt
    
    Argument:
    angle -- a number (integer or float)
    
    Turn turtle left by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)
    
    Example:
    >>> heading()
    22.0
    >>> left(45)
    >>> heading()
    67.0

>>> debo.lt(60)
>>> help(turtle.right)
Help on function right in module turtle:

right(angle)
    Turn turtle right by angle units.
    
    Aliases: right | rt
    
    Argument:
    angle -- a number (integer or float)
    
    Turn turtle right by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)
    
    Example:
    >>> heading()
    22.0
    >>> right(45)
    >>> heading()
    337.0

>>> debo.rt(90)
>>> 