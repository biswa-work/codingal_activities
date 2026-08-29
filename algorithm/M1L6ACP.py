import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colour Loop Artwork")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def petal():
    t.begin_fill()
    for i in range(2):
        t.circle(100, 60)
        t.left(120)
    t.end_fill()

for i in range(36):
    t.color(colors[i % len(colors)])
    petal()
    t.left(10)

turtle.done()
