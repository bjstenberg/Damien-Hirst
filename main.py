import turtle as turtle_module
from turtle import Screen
import random

turtle_module.colormode(255)
jim = turtle_module.Turtle()
jim.pensize(0)
jim.hideturtle()
jim.penup()
jim.speed("fastest")

color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
    (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
    (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
    (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
    (176, 192, 209)
]

jim.setheading(225)
jim.forward(310)
jim.setheading(0)

num_of_dots = 100

for dots in range(1, num_of_dots + 1):
    jim.dot(20, random.choice(color_list))
    jim.forward(50)
    if dots % 10 == 0:
        jim.setheading(90)
        jim.forward(50)
        jim.setheading(180)
        jim.fd(500)
        jim.setheading(0)



screen = Screen()
screen.exitonclick()