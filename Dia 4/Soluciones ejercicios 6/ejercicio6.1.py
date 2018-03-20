import turtle
import math
x = 1080
y = 720
h = math.hypot(x,y)
ang = math.degrees(math.atan(y/x))
s = turtle.Screen()
turtle.setup(x,y)
t = turtle.Turtle()
t.resizemode('user')
t.turtlesize(3, 3)
t.penup()
t.setx(-x/2)
t.sety(y/2)
t.pendown()
t.right(ang) 
t.forward(h)
t.penup()
t.right(180 - 2*ang)
t.sety(y/2)
t.pendown()
t.forward(h)

turtle.mainloop()