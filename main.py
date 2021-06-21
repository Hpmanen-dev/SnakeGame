import turtle
from snake import Snake
from apple import Apple

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title('Snake Game')

Body = Snake()
apple = Apple()

Body.add_newbody()
Body.add_newbody()
Body.add_newbody()
Body.add_newbody()



screen.listen()
screen.onkey(Body.up, "Up")
screen.onkey(Body.down, "Down")
screen.onkey(Body.left, "Left")
screen.onkey(Body.right, "Right")

active = True
while active:
    screen.update()
    Body.move()
    if Body.head.distance(apple.apple) < 19:
        apple.collide()
        Body.add_newbody()

turtle.done()