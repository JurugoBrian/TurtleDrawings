import turtle                    # Importing the turtle library
import tkinter as TK
window_color = input("Enter the desired color for your windows: ")
alex_color = input("Alex, enter your color please: ")
alex_pensize_str = input("Alex, enter your pen size please: ")
window = turtle.Screen()         # Drawing a screen
window.bgcolor(window_color)
alex = turtle.Turtle()           # Creating a turtle object
alex.color(alex_color)
alex_pensize = int(alex_pensize_str)
alex.pensize(alex_pensize)
alex.forward(150)                # Alex moves forward by 150 units
alex.left(90)                    # Alex turns left90 degrees
alex.forward(75)                 # Alex moves forward by 75 units
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)
window.exitonclick()