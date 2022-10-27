import turtle

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

def turtleArt(turtle, number):
    """
        This function checks which bitmap number is being run and then calls the pixel() function in order to draw the correct color cube.

        args: turtle (this calls the turtle object named in the parameter and inserts it as a parameter into the pixel function, as well as to skip the cube if the number is 0 (blank)) number (this is an int parameter that is used to determine what the fill color of the drawn square should be)
        return: the "return" of this function is simply to run the pixel function
    """
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








