import turtle
from turtle import *
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#starting_position = [(0, 0), (-20, 0), (-40, 0)]  #tuple

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)

  snake.move()




screen.exitonclick()