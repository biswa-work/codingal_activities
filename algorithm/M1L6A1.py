import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

colors = ["cyan", "magenta", "lime", "orange", "blue", "red"]

for i in range(120):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 2)
    t.right(59)

t.penup()
t.goto(0, 0)
t.pendown()
t.color("gold")
t.begin_fill()

for i in range(5):
    t.forward(150)
    t.right(144)

t.end_fill()

for i in range(36):
    t.color(colors[i % len(colors)])
    t.begin_fill()
    t.circle(80, 60)
    t.left(120)
    t.circle(80, 60)
    t.left(50)
    t.end_fill()

turtle.done()
