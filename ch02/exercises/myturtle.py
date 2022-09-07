import turtle

turtle73 = turtle.Turtle()
turtle73.shape("turtle")

turtle73.pencolor("purple")
turtle73.fillcolor("purple")
#Sets the line color and fill color of the turtle to purple. 
turtle73.begin_fill()
turtle73.forward(50)
turtle73.right(90)
turtle73.forward(50)
turtle73.right(90)
turtle73.forward(50)
turtle73.right(90)
turtle73.forward(50)
turtle73.right(90)
turtle73.end_fill()
#Begins the fill, draws the shape of the square, and fills it in at the end. 

turtle73.penup()
#Lifts the pen, allowing the turtle to move without drawing a line behind it. 
turtle73.back(80)
turtle73.pencolor("seagreen")
turtle73.fillcolor("seagreen")
turtle73.pendown()
#Sets the line color and fill color to red, and puts the pen back down, allowing the turtle to draw again. 
turtle73.begin_fill()
turtle73.forward(50)
turtle73.right(90)
turtle73.forward(50)
turtle73.right(90)
turtle73.forward(50)
turtle73.right(90)
turtle73.forward(50)
turtle73.right(90)
turtle73.end_fill()
#Begins the fill, draws the shape of the square, and fills it in at the end.
 

turtle.done()
