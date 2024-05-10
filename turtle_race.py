import turtle
from turtle import  Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinate = [-80, -40, 0 , 40, 80, 120]
turtles = []
is_race_done = False

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(-240, y_coordinate[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_done = True

while is_race_done:
    for turtle in turtles:
        if turtle.xcor() > 240:
            is_race_done = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner! ")
        random_dist = random.randint(0,10)
        turtle.forward(random_dist)

screen.exitonclick()