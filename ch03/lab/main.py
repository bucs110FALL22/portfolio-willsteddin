import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed("slow")
leonardo.speed("slow")


michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

michelangelo.fd(random.randrange(0,101))
leonardo.fd(random.randrange(0,101))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


for i in [10]*10:
  michelangelo.fd(random.randrange(0,11))
  leonardo.fd(random.randrange(0,11))
  
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window.exitonclick()

# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()

coords = []
sideLength = 100
xoffset = 300
yoffset = 180
#numSides = [3, 4, 6, 9, 360]
pygame.display.flip()
pygame.time.wait(2000)

numSides = []
numShapes = int(input("How many shapes would you like to draw? "))
for i in range(numShapes):
  shape = int(input("Please enter how many sides you would like this shape to be: "))
  numSides.append(shape)
  

for _ in numSides:
  for i in range(_):
    theta = (2.0 * math.pi * (i/_) )
    x = sideLength * math.cos(theta) + xoffset
    y = sideLength * math.sin(theta) + yoffset
    coords.append((x,y))
  pygame.display.flip()
  pygame.draw.polygon(window, "orchid", coords, width=0)
  pygame.display.flip()
  pygame.time.wait(1500)
  window.fill("black")
  pygame.display.flip()
  pygame.time.wait(1000)
  coords = []