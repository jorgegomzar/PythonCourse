import turtle

turtle.setup(800, 600)
l = 100
ang = 150
t = turtle.Turtle()
t.left(75)
for i in range(2):
	t.right(ang)
	t.forward(l)
	t.left(ang)
	t.forward(l)

turtle.mainloop()