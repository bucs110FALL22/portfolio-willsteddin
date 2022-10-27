import turtle

def pixel(turtle, color):
    turtle.pendown()
    turtle.pencolor("black")
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(25)
        turtle.right(90)
    turtle.end_fill()
    turtle.fd(25)

def turtleArt(turtle, number):
        turtle.penup()
        if number == 0:
            turtle.penup()
            turtle.fd(25)
        elif number == 1:
            pixel(turtle, "saddlebrown")
        elif number == 2:
            pixel(turtle, "navajowhite")
        elif number == 3:
            pixel(turtle, "black")

def main():
    goombaBitmap = [[0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0], [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0], [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0], [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0], [0,0,1,3,3,1,1,1,1,1,1,3,3,1,0,0], [0,1,1,1,2,3,1,1,1,1,3,2,1,1,1,0], [0,1,1,1,2,3,3,3,3,3,3,2,1,1,1,0], [1,1,1,1,2,3,2,1,1,2,3,2,1,1,1,1], [1,1,1,1,2,2,2,1,1,2,2,2,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [0,1,1,1,1,2,2,2,2,2,2,1,1,1,1,0], [0,0,0,0,2,2,2,2,2,2,2,2,0,0,0,0], [0,0,3,3,2,2,2,2,2,2,2,2,3,3,0,0], [0,3,3,3,3,3,2,2,2,2,3,3,3,3,3,0], [0,3,3,3,3,3,3,2,2,3,3,3,3,3,3,0], [0,0,3,3,3,3,3,0,0,3,3,3,3,3,0,0]]
    turtle.screensize(canvwidth=400,canvheight=400,bg="white")
    smb1 = turtle.Turtle()
    smb1.ht()
    smb1.speed(0)
    origin = (-200,200)
    count = 0
    for line in goombaBitmap:
        smb1.penup()
        smb1.setpos(origin[0], origin[1]-(count*25))
        for block in line:
            turtleArt(smb1, block)
        count += 1
    turtle.exitonclick()

main()








