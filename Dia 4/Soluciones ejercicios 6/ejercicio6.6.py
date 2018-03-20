import turtle

turtle.setup(800, 600)
t = turtle.Turtle()
t.hideturtle()
t.shape('turtle')
t.penup()
t.sety(-300)
t.left(90)
t.fillcolor('green')
t.turtlesize(5, 5)
t.showturtle()
for y in range(-300, 300, 1):
	t.sety(y)
	if y == 0:
		t.fillcolor('blue')

turtle.mainloop()