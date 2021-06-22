from turtle import Turtle
import random

class Apple:
    def __init__(self):
        self.apple = Turtle("square")
        self.apple.color("Red")
        self.apple.penup()
        self.apple.speed('fastest')
        self.apple.goto(20, 20)
    
    def collide(self):
        new_x = random.randrange(-300, 301, 20)
        new_y = random.randrange(-300, 301, 20)
        
        self.apple.goto(new_x, new_y)
        