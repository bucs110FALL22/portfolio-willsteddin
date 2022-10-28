import turtle
import random

def pixel(turtle, color):
    """
        This function draws a small cube, or a "pixel" on the screen using the turtle module. It chooses the color of the cube based on the parameters and then moves on to the next spot to start again. 

        args: turtle (this calls the turtle object named in the parameter and uses it to draw the square), color (this is a string, and is used to determine the fill color of the cube)
        return: this function returns a drawn cube on the turtle screen
    """
    turtle.pendown()
    turtle.pencolor("black")
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(25)
        turtle.right(90)
    turtle.end_fill()
    turtle.fd(25)

def turtleArt(turtle, number, name):
    """
        This function checks which bitmap number is being run and then calls the pixel() function in order to draw the correct color cube.

        args: turtle (this calls the turtle object named in the parameter and inserts it as a parameter into the pixel function, as well as to skip the cube if the number is 0 (blank)) number (this is an int parameter that is used to determine what the fill color of the drawn square should be)
        return: the "return" of this function is simply to run the pixel function
    """
    if name == "goomba":
        color1, color2, color3 = "saddlebrown", "navajowhite", "black"
    if name == "mushroom":
        color1, color2, color3, color4 = "red", "navajowhite", "black", "white"
    if name == "fireflower":
        color1, color2, color3, color4, color5 = "darkorange", "yellow", "black", "white", "lawngreen" 
    turtle.penup()
    if name == "coinblock":
        color1, color2, color3 = "darkorange", "gold", "black"
    if number == 0:
        turtle.penup()
        turtle.fd(25)
    elif number == 1:
        pixel(turtle, color1)
    elif number == 2:
        pixel(turtle, color2)
    elif number == 3:
        pixel(turtle, color3)
    elif number == 4:
        pixel(turtle, color4)
    elif number == 5:
        pixel(turtle, color5)

def artChoose(name):
    bitmapDict = {
        "goomba": [[0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0], [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0], [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0], [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0], [0,0,1,3,3,1,1,1,1,1,1,3,3,1,0,0], [0,1,1,1,2,3,1,1,1,1,3,2,1,1,1,0], [0,1,1,1,2,3,3,3,3,3,3,2,1,1,1,0], [1,1,1,1,2,3,2,1,1,2,3,2,1,1,1,1], [1,1,1,1,2,2,2,1,1,2,2,2,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [0,1,1,1,1,2,2,2,2,2,2,1,1,1,1,0], [0,0,0,0,2,2,2,2,2,2,2,2,0,0,0,0], [0,0,3,3,2,2,2,2,2,2,2,2,3,3,0,0], [0,3,3,3,3,3,2,2,2,2,3,3,3,3,3,0], [0,3,3,3,3,3,3,2,2,3,3,3,3,3,3,0], [0,0,3,3,3,3,3,0,0,3,3,3,3,3,0,0]], 
        "mushroom": [[0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0], [0,0,0,3,3,1,1,1,1,4,4,3,3,0,0,0], [0,0,3,4,4,1,1,1,1,4,4,4,4,3,0,0], [0,3,4,4,1,1,1,1,1,1,4,4,4,4,3,0],[0,3,4,1,1,4,4,4,4,1,1,4,4,4,3,0],[3,1,1,1,4,4,4,4,4,4,1,1,1,1,1,3],[3,4,1,1,4,4,4,4,4,4,1,1,4,4,1,3],[3,4,1,1,4,4,4,4,4,4,1,4,4,4,4,3],[3,4,4,1,1,4,4,4,4,1,1,4,4,4,4,3],[3,4,4,1,1,1,1,1,1,1,1,1,4,4,1,3],[3,4,1,1,3,3,3,3,3,3,3,3,1,1,1,3],[0,3,3,3,2,2,3,2,2,3,2,2,3,3,3,0],[0,0,3,2,2,2,3,2,2,3,2,2,2,3,0,0],[0,0,3,2,2,2,2,2,2,2,2,2,2,3,0,0],[0,0,0,3,2,2,2,2,2,2,2,2,3,0,0,0],[0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0]], 
        "fireflower": [[0,0,0,3,3,3,3,3,3,3,3,3,3,0,0,0], [0,3,3,3,1,1,1,1,1,1,1,1,3,3,3,0], [3,3,1,1,1,2,2,2,2,2,2,1,1,1,3,3], [3,1,1,2,2,2,3,4,4,3,2,2,2,1,1,3], [3,1,1,2,2,2,3,4,4,3,2,2,2,1,1,3], [3,1,1,1,1,2,2,2,2,2,2,1,1,1,1,3], [3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,3], [0,3,3,3,1,1,1,1,1,1,1,1,3,3,3,0], [0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0], [0,0,3,3,0,0,3,5,5,3,0,0,3,3,0,0], [0,3,5,5,3,0,3,5,5,3,0,3,5,5,3,0], [0,3,5,5,5,3,3,5,5,3,3,5,5,5,3,0], [0,0,3,5,5,5,3,5,5,3,5,5,5,3,0,0], [0,0,3,5,5,5,3,5,5,3,5,5,5,3,0,0], [0,0,0,3,3,5,5,5,5,5,5,3,3,0,0,0], [0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0]], 
        "coinblock": [[3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3], [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3], [1,2,3,2,2,2,2,2,2,2,2,2,2,3,2,3], [1,2,2,2,2,1,1,1,1,1,2,2,2,2,2,3], [1,2,2,2,1,1,3,3,3,1,1,2,2,2,2,3], [1,2,2,2,1,1,3,2,2,1,1,3,2,2,2,3], [1,2,2,2,1,1,3,2,2,1,1,3,2,2,2,3], [1,2,2,2,2,3,3,2,1,1,1,3,2,2,2,3], [1,2,2,2,2,2,2,1,1,3,3,3,2,2,2,3], [1,2,2,2,2,2,2,1,1,3,2,2,2,2,2,3], [1,2,2,2,2,2,2,2,3,3,2,2,2,2,2,3], [1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,3], [1,2,2,2,2,2,2,1,1,3,2,2,2,2,2,3], [1,2,3,2,2,2,2,2,3,3,2,2,2,3,2,3], [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3], [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]}
    result = bitmapDict[name]
    return result


def main():
    turtle.screensize(canvwidth=400,canvheight=400,bg="white")
    smb1 = turtle.Turtle()
    smb1.ht()
    smb1.speed(0)
    origin = (-200,200)
    count = 0
    drawing = "coinblock"
    for line in artChoose(drawing):
        smb1.penup()
        smb1.setpos(origin[0], origin[1]-(count*25))
        for block in line:
            turtleArt(smb1, block, drawing)
        count += 1
    turtle.exitonclick()

main()



