import time

class Animal:
    """ 
    Class for representing animals in a shelter. 
    """
    def __init__(self, name, type):
      self.name = name
      self.type = type
      self.id = time.strftime("%d%m%M%S")
      self.arrived = time.strftime("%d/%m/%Y")
      self.adopted = False

    def setAdopted(self):
      self.adopted = time.strftime("%d/%m/%Y")
    
    def __str__(self):
      resultStr = f"{self.name}[{self.type}]"
      resultStr += f"\narrived: {self.arrived}"
      resultStr += f"\nadopted: {self.adopted}"
      return resultStr
    
    

