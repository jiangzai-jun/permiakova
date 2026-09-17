import turtle

t = turtle.Turtle()
t.speed(0)

sides = 360
length = 2
angle = 360 / sides

for _ in range(sides) :
    t.forward(length)
    t.left(angle)

turtle.done()


