import turtle
from snake import Snake
from apple import Apple

screen = turtle.Screen()
screen.setup(width=620, height=620)
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
    if Body.head.xcor() > 300 or Body.head.xcor() < -300:
        print("Game Over!")
        break
    if Body.head.ycor() > 300 or Body.head.ycor() < -300:
        print("Game Over!")
        break
    Body.move()
    if Body.head.distance(apple.apple) < 19:
        apple.collide()
        Body.add_newbody()
    


turtle.done()
