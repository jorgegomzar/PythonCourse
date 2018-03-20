import turtle
turtle.setup(800, 600)

s = turtle.Screen()
s.bgcolor('black')
s.title('Arc reactor by Beno')
t = turtle.Turtle()

turtle.register_shape('pol', ((13, -3), (10, -1),(10, 1), (13, 3)))
turtle.register_shape('rod', ((12, -2), (10, -1),(10, 1), (12, 2)))
t.shape('rod')
t.resizemode('user')
t.turtlesize(15, 15)
t.hideturtle()
for angle in range (0, 360, 1):
	t.setheading(angle)
	t.fillcolor('darkgrey')
	t.stamp()

t.shape('pol')
t.resizemode('user')
t.turtlesize(15, 15)

for angle in range (0, 360, 60):
	t.setheading(angle)
	t.fillcolor('grey')
	t.stamp()

t.setx(0)
t.sety(0)
turtle.colormode(255)
r, g, b = [0, 220, 255]
for tam in range (300, 0, -20):
	t.dot(tam+1, r, g, b)
	r = r + 15
s.bgcolor(115, 0, 0)
turtle.mainloop()
