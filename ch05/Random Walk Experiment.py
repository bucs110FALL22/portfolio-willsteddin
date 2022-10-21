import random
import turtle
import math

def markov(start, end, bounds):
    """
    This is a function that simulates a random walk event.

    args: start (tuple, starting coordinates for turtle), end (tuple, endpoint for random walk simulation), bounds (tuple, sets the size of the screen for the random walk event to occur on)
    return: turtle drawing loop that self-perpetuates until the turtle reaches the assigned endpoint
    """
    monte = turtle.Turtle()
    monte.shape("circle")
    monte.shapesize(1, 1, 0)
    monte.setpos(start)
    turtle.screensize(canvwidth=bounds[0], canvheight=bounds[1], bg = "snow")
    steps = 0
    monte.speed(0)
    while monte.pos() != end:
        direction = random.randrange(4)
        if direction == 0: 
            monte.fd(10)
            steps += 1
        elif direction == 1:
            monte.left(90)
            monte.fd(10)
            monte.right(90)
            steps += 1
        elif direction == 2:
            monte.right(90)
            monte.forward(10)
            monte.left(90)
            steps += 1
        elif direction == 3:
            monte.right(180)
            monte.fd(10)
            monte.right(180)
            steps += 1
    return steps



def markov2(start, end):
    monte2 = turtle.Turtle()
    turtle.screensize(canvwidth = 500, canvheight = 500, bg = "palevioletred")
    monte2.speed(10)
    steps = 0
    monte2.setposition(x = start[0], y = start[1])
    stop = (end[0], end[1])
    print(stop)
    print(monte2.pos())
    print((float(stop[0]), float(stop[1])))
    while monte2.pos() != (float(stop[0]), float(stop[1])):
        monte2.fd(10)
        steps += 1
    return

def main():
    res = markov2((0,0), (0, 70))
    # print(res)
main()   
