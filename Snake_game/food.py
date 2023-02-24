from turtle import Turtle
import random

class Food(Turtle): #adding the super call Turtle
  def __init__(self):
    super().__init__()  #inherit from super class Tutle
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_wid=0.7, stretch_len=0.7)
    self.color("green")
    self.speed("fastest")
    self.refresh()

  def refresh(self):
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    self.goto(random_x, random_y)



