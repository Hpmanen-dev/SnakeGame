from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = [Turtle("square")]
        self.head = self.body[0]
        self.head.speed('fast')
        self.head.penup()
    
    def add_newbody(self):
        new_body = Turtle("square")
        new_body.speed('fastest')
        new_body.penup()
        tailtip = self.body[len(self.body) - 1]
        new_x = tailtip.xcor() - 20
        new_y = tailtip.ycor()
        new_body.goto(new_x, new_y)
        self.body.append(new_body)



    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def move(self):
        time.sleep(0.075)
        for number in range(len(self.body) - 1, 0, -1):
            new_x = self.body[number - 1].xcor()
            new_y = self.body[number - 1].ycor()
            self.body[number].goto(new_x, new_y)
        self.head.forward(20)


