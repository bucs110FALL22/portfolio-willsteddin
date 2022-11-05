import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    self.rect = Rectangle(x, y, h, w)
    self.image = str(filename)

  def getRect(self):
    """
      This method simply returns the rectangle object created in the init.

      args: Surface class object (self)
      return: Rectangle class object
    """
    return self.rect