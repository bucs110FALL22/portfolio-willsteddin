import turtle

class Graph:

    def __init__(self):
        self.points = []
        self.plotter = turtle.Turtle()
        self.plotter.up()
        

    def addPoint(self, point):
        self.points.append(point)

    def plot(self):
        for p in self.points:
            self.plotter.color(p.color)
            self.plotter.goto(p.x, p.y)
            self.plotter.dot(5)
            turtle.exitonclick()
    
    def __str__(self):
        pointStr = ""
        for p in self.points:
            pointStr += f"{self.x}, {self.y}"
        return f"{self.title}: {pointStr}"




