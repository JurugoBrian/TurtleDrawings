import turtle
window = turtle.Screen()
window.bgcolor("Green")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)      # Tess completes making a triangle

tess.left(180)
tess.forward(80)


alex = turtle.Turtle()
alex.pensize(3)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)     # Alex completes a rectangle

window.exitonclick()
