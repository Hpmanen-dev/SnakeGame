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
        self.head.speed('fastest')
        self.head.penup()
        self.pos = self.head.pos()
    
    def add_newbody(self):
        new_body = Turtle("square")
        new_body.speed('fastest')
        new_body.penup()
        head_position = self.body[0].pos()
        y = list(head_position)
        if self.head.heading() == RIGHT:
            y[0] -= 20 * len(self.body)
        elif self.head.heading() == LEFT:
            y[0] += 20 * len(self.body)
        elif self.head.heading() == UP:
            y[1] += 20 * len(self.body)
        else:
            y[1] -= 20 * len(self.body)

        self.pos = tuple(y)
        new_body.goto(self.pos)
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
        time.sleep(0.1)
        for number in range(len(self.body) - 1, 0, -1):
            new_x = self.body[number - 1].xcor()
            new_y = self.body[number - 1].ycor()
            self.body[number].goto(new_x, new_y)
        self.head.forward(20)


