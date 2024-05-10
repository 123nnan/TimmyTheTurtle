import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.pensize(10)
# tim.turtlesize()
turtle.colormode(255)
tim.speed(0)

def random_color():
    """Return random color in r, g ,b"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g ,b)
    return color
# color = ['red', 'yellow', 'blue', 'green', 'black', 'white', 'cyan', 'orange', 'CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray']
direction = [0, 90, 180, 270]

number_of_dots = 100
y = 40
for dot_count in range(1, (number_of_dots + 1)):
    tim.dot(20, random_color())
    tim.pu()
    tim.fd(40)

    if dot_count % 10 == 0:
        tim.setpos(0, y)
        y += 40

screen = Screen()
screen.exitonclick()