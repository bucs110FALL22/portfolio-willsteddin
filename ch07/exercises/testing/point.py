class Point: 
    def __init__(self, x=0, y=0, color=[255,0,0]):
        self.x = x
        self.y = y
        if color == "green":
            print("You are a bad person.")
            color == "blue"
        self.color = color
    
    def setToCompColor(self):
        redComp = 255 - self.color[0]
        blueComp = 255 - self.color[1]
        greenComp = 255 - self.color[2]
        self.color = [redComp, blueComp, greenComp]

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        self.setToCompColor()
        return Point(mx, my, self.color)