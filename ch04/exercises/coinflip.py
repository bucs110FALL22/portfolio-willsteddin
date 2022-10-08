import turtle
import random

fcg = turtle.Turtle()
fcg.shape("turtle")
fcg.color("crimson")
fcg.speed(0)
fcg.setpos(0, 0)
turtle.screensize(canvwidth=500, canvheight=500, bg="palevioletred")
canvwidth = turtle.window_width()
canvheight = turtle.window_height()

while abs(fcg.xcor()) < (canvwidth / 2) and abs(fcg.ycor()) < (canvheight / 2):
    result = random.randrange(2)
    if result == 1:
        fcg.left(90)
        fcg.forward(1)
        print("Heads")
    else:
        fcg.right(90)
        fcg.forward(1)
        print("Tails")

print(fcg.pos(), (canvwidth / 2, canvheight / 2))
turtle.Screen().exitonclick()
