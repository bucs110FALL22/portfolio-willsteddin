from point import Point
from graph import Graph



def main():
    p1 = Point()
    print(p1.x, p1.y, p1.color)
    p1.setToCompColor()
    print(p1.x, p1.y, p1.color)
    p2 = Point(6, 6, [0, 0, 255])
    p3 = p1.halfway(p2)
    print(p3.x, p3.y, p3.color)

    graph = Graph()
    graph.addPoint(p1)
    graph.addPoint(p2)
    graph.addPoint(p3)
    graph.plot()


main()