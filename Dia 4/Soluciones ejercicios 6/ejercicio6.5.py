import turtle

turtle.setup(800, 600)
t = turtle.Turtle()
t.shape('turtle')
t.penup()
t.hideturtle()
t.sety(-300)
t.left(90)
tam1 = 10
t.fillcolor('green')
t.showturtle()
for y in range(-300, 300, 1):
	t.turtlesize(tam1, tam1)
	t.sety(y)
	tam1 = tam1 - 1/60

turtle.mainloop()