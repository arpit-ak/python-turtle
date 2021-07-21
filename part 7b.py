
def draw_circle(x,y,color,rad):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()
    t.down()
import turtle
t=turtle.Turtle()
draw_circle(0,-50,"green",50)
draw_circle(200,200,"orange",50)
draw_circle(-200,200,"blue",50)
draw_circle(-200,-200,"red",-50)
draw_circle(200,-200,"yellow",-50)



