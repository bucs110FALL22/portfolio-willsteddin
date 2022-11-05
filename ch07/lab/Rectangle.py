class Rectangle:
  def __init__(self, x, y, h, w):
    for i in [x, y, h, w]:
      if i < 0:
        i = 0
    self.x = x
    self.y = y
    self.height = h
    self.width = w

  def __str__(self):
    """
      This method returns the x and y coordinates of a rectangles upper left corner, as well as it's height and width, in a string. 

      args: self (rectangle class object)
      return: str
    """
    return f"(x: {self.x}, y: {self.y}) Height: {self.height}, Width = {self.width}"