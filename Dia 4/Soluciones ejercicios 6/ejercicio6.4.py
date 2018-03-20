import turtle

turtle.setup(800, 600)
c1 = turtle.Turtle()
x = 50
colores = ['red', 'green', 'blue']
for i in range(3):
	c1.pendown()
	if i < 3:
		c1.pencolor(colores[i])
	c1.circle(x)
	c1.right(90)
	c1.penup()
	c1.forward(x)
	c1.left(90)
	x = 2 * x

turtle.mainloop()