import turtle
import pygame

pygame.init()

def pixel(turtle, color, pixelsize):
    """
        This function draws a small cube, or a "pixel" on the screen using the turtle module. It chooses the color of the cube based on the parameters and then moves on to the next spot to start again. 

        args: turtle (this calls the turtle object named in the parameter and uses it to draw the square), color (this is a string, and is used to determine the fill color of the cube)
        return: None
    """
    turtle.pendown()
    turtle.pencolor("black")
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(pixelsize)
        turtle.right(90)
    turtle.end_fill()
    turtle.fd(pixelsize)

def turtleArt(turtle, number, name, pixelsize):
    """
        This function checks which bitmap number is being run and then calls the pixel() function in order to draw the correct color cube.

        args: turtle (this calls the turtle object named in the parameter and inserts it as a parameter into the pixel function, as well as to skip the cube if the number is 0 (blank)) number (this is an int parameter that is used to determine what the fill color of the drawn square should be)
        return: None
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
        turtle.fd(pixelsize)
    elif number == 1:
        pixel(turtle, color1, pixelsize)
    elif number == 2:
        pixel(turtle, color2, pixelsize)
    elif number == 3:
        pixel(turtle, color3, pixelsize)
    elif number == 4:
        pixel(turtle, color4, pixelsize)
    elif number == 5:
        pixel(turtle, color5, pixelsize)

def artChoose(name):
    """
        This function is used to input the proper bitmap into the turtleArt function, by utilizing a dictionary. 

        args: name (str, is used as a key to check against the dictionary)
        return: list (the bitmap, a list of lists to input colors into the art function)
    """
    bitmapDict = {
        "goomba": [[0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0], [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0], [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0], [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0], [0,0,1,3,3,1,1,1,1,1,1,3,3,1,0,0], [0,1,1,1,2,3,1,1,1,1,3,2,1,1,1,0], [0,1,1,1,2,3,3,3,3,3,3,2,1,1,1,0], [1,1,1,1,2,3,2,1,1,2,3,2,1,1,1,1], [1,1,1,1,2,2,2,1,1,2,2,2,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [0,1,1,1,1,2,2,2,2,2,2,1,1,1,1,0], [0,0,0,0,2,2,2,2,2,2,2,2,0,0,0,0], [0,0,3,3,2,2,2,2,2,2,2,2,3,3,0,0], [0,3,3,3,3,3,2,2,2,2,3,3,3,3,3,0], [0,3,3,3,3,3,3,2,2,3,3,3,3,3,3,0], [0,0,3,3,3,3,3,0,0,3,3,3,3,3,0,0]], 
        "mushroom": [[0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0], [0,0,0,3,3,1,1,1,1,4,4,3,3,0,0,0], [0,0,3,4,4,1,1,1,1,4,4,4,4,3,0,0], [0,3,4,4,1,1,1,1,1,1,4,4,4,4,3,0],[0,3,4,1,1,4,4,4,4,1,1,4,4,4,3,0],[3,1,1,1,4,4,4,4,4,4,1,1,1,1,1,3],[3,4,1,1,4,4,4,4,4,4,1,1,4,4,1,3],[3,4,1,1,4,4,4,4,4,4,1,4,4,4,4,3],[3,4,4,1,1,4,4,4,4,1,1,4,4,4,4,3],[3,4,4,1,1,1,1,1,1,1,1,1,4,4,1,3],[3,4,1,1,3,3,3,3,3,3,3,3,1,1,1,3],[0,3,3,3,2,2,3,2,2,3,2,2,3,3,3,0],[0,0,3,2,2,2,3,2,2,3,2,2,2,3,0,0],[0,0,3,2,2,2,2,2,2,2,2,2,2,3,0,0],[0,0,0,3,2,2,2,2,2,2,2,2,3,0,0,0],[0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0]], 
        "fireflower": [[0,0,0,3,3,3,3,3,3,3,3,3,3,0,0,0], [0,3,3,3,1,1,1,1,1,1,1,1,3,3,3,0], [3,3,1,1,1,2,2,2,2,2,2,1,1,1,3,3], [3,1,1,2,2,2,3,4,4,3,2,2,2,1,1,3], [3,1,1,2,2,2,3,4,4,3,2,2,2,1,1,3], [3,1,1,1,1,2,2,2,2,2,2,1,1,1,1,3], [3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,3], [0,3,3,3,1,1,1,1,1,1,1,1,3,3,3,0], [0,0,0,0,3,3,3,3,3,3,3,3,0,0,0,0], [0,0,3,3,0,0,3,5,5,3,0,0,3,3,0,0], [0,3,5,5,3,0,3,5,5,3,0,3,5,5,3,0], [0,3,5,5,5,3,3,5,5,3,3,5,5,5,3,0], [0,0,3,5,5,5,3,5,5,3,5,5,5,3,0,0], [0,0,3,5,5,5,3,5,5,3,5,5,5,3,0,0], [0,0,0,3,3,5,5,5,5,5,5,3,3,0,0,0], [0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0]], 
        "coinblock": [[3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3], [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3], [1,2,3,2,2,2,2,2,2,2,2,2,2,3,2,3], [1,2,2,2,2,1,1,1,1,1,2,2,2,2,2,3], [1,2,2,2,1,1,3,3,3,1,1,2,2,2,2,3], [1,2,2,2,1,1,3,2,2,1,1,3,2,2,2,3], [1,2,2,2,1,1,3,2,2,1,1,3,2,2,2,3], [1,2,2,2,2,3,3,2,1,1,1,3,2,2,2,3], [1,2,2,2,2,2,2,1,1,3,3,3,2,2,2,3], [1,2,2,2,2,2,2,1,1,3,2,2,2,2,2,3], [1,2,2,2,2,2,2,2,3,3,2,2,2,2,2,3], [1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,3], [1,2,2,2,2,2,2,1,1,3,2,2,2,2,2,3], [1,2,3,2,2,2,2,2,3,3,2,2,2,3,2,3], [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3], [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]
        }
    result = bitmapDict[name]
    return result


def draw(drawing, canvsize):
    """
        This function activates the drawing and carries it out. It initializes the screen and the turtle, and sets the speed to ensure the drawing is completed quickly. 

        args: name (str, is input into artChoose() to determine which drawing to carry out), canvsize** (int, sets the size of the canvas.)
        **canvsize must be set to a multiple of 16 for the drawing to work properly
        return: None
    """
    turtle.screensize(canvwidth=canvsize,canvheight=canvsize,bg="white")
    smb1 = turtle.Turtle()
    smb1.ht()
    smb1.speed(0)
    origin = (-1*(canvsize/2),(canvsize/2))
    count = 0
    pixelsize = canvsize/16
    for line in artChoose(drawing):
        smb1.penup()
        smb1.setpos(origin[0], origin[1]-(count*(canvsize/16)))
        for block in line:
            turtleArt(smb1, block, drawing, pixelsize)
        count += 1
    turtle.exitonclick()


def main():
    bounds = 400
    selection = True
    font = pygame.font.Font(None, 30)
    window = pygame.display.set_mode((400,400))
    window.fill("white")
    rectGoomba = ((25,25), (150,150))
    goombaButtonBox = pygame.Rect(rectGoomba)
    msgGoomba = font.render("Goomba", True, "black")
    rectMushroom = ((225, 25), (150,150))
    mushroomButtonBox = pygame.Rect(rectMushroom)
    msgMushroom = font.render("Mushroom", True, "black")
    rectFireflower = ((25, 225), (150,150))
    fireflowerButtonBox = pygame.Rect(rectFireflower)
    msgFireflower = font.render("Fire Flower", True, "black")
    rectCoinblock = ((225,225), (150,150))
    coinblockButtonBox = pygame.Rect(rectCoinblock)
    msgCoinblock = font.render("Coin Block", True, "black")
    pygame.display.flip()
    pygame.draw.rect(window, "saddlebrown", rectGoomba)
    window.blit(msgGoomba, (55,90))
    pygame.draw.rect(window, "red", rectMushroom)
    window.blit(msgMushroom, (250, 90))
    pygame.draw.rect(window, "green", rectFireflower)
    window.blit(msgFireflower, (45,290))
    pygame.draw.rect(window, "gold", rectCoinblock)
    window.blit(msgCoinblock, (245,290))
    pygame.display.flip()
    while selection:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClickPos = event.pos
                if goombaButtonBox.collidepoint(mouseClickPos): 
                    window.fill("white")
                    pygame.display.flip()
                    draw("goomba", bounds)
                    selection = False
                elif mushroomButtonBox.collidepoint(mouseClickPos):
                    window.fill("white")
                    pygame.display.flip()
                    draw("mushroom", bounds)
                    selection = False
                elif fireflowerButtonBox.collidepoint(mouseClickPos):
                    window.fill("white")
                    pygame.display.flip()
                    draw("fireflower", bounds)
                    selection = False
                elif coinblockButtonBox.collidepoint(mouseClickPos):
                    window.fill("white")
                    pygame.display.flip()
                    draw("coinblock", bounds)
                    selection = False


main()