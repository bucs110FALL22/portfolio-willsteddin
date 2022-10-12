import turtle


def drawEqShape(turtle, numSides, lenSides):
    for i in range(numSides):
        fcg.fd(lenSides)
        fcg.left(360 / numSides)


fcg = turtle.Turtle()
fcg.shape("turtle")
fcg.color("green")
numSides = int(input("How many sides? "))
lenSides = int(input("How long is each side? "))
drawEqShape(fcg, numSides, lenSides)

turtle.exitonclick()
