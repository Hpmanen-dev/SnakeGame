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
        new_x = random.randint(-300, 300)
        while new_x % 20 != 0:
            new_x = random.randint(-300, 300)

        new_y = random.randint(-300, 300)
        while new_y % 20 != 0:
            new_y = random.randint(-300, 300)
        
        self.apple.goto(new_x, new_y)
        