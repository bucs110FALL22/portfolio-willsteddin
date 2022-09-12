import turtle

sides_num = int(input("Please enter how many sides you would like your shape to have: "))
sides_len = float(input("Please input how long you would like each side of your shape to be: "))
color = input("Please input what color you would like your shape to be: ")
print(sides_num, sides_len)
angle = 360/sides_num


turtle13 = turtle.Turtle()


turtle13.pencolor(color)
turtle13.fillcolor(color)
turtle13.begin_fill()

for i in [angle] * sides_num:
  turtle13.forward(sides_len)
  turtle13.left(angle)
  
turtle13.end_fill()

turtle.exitonclick()
turtle.done()