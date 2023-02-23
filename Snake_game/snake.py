from turtle import Turtle, Screen
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)] #IN PYTHON, ALL CONSTANTS ARE WRITTEN IN CAPITAL
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:  #we can now create a snake objects and each time we create obvject it creates 3 segments
  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head = self.segments[0] #the head of the snake

  def create_snake(self):
    for position in STARTING_POSITION:
      new_segment = Turtle("square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment)


  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)


  def up(self):
    if self.head.heading() != DOWN: #BE CAREFUL ITS HEADING() METHOD NOT JUST HEADING
       self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(LEFT)




