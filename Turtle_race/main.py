import turtle
from turtle import *
import random
screen = Screen()
all_turtle = []

screen.setup(width=500,height=400)  #to setup width and height
user_bet= screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
print(user_bet)

is_race_on = False

y_position= [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0,6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.goto(x=-230, y=y_position[turtle_index]) #to give value to x and y axis
  new_turtle.color(colors[turtle_index])
  all_turtle.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtle:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"Congratulations! You won the bet. The  {winning_color} is the winner.")
      else:
        print("You have lost.")
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)

screen.exitonclick()
