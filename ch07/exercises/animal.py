import time

class Animal:
    """ 
    Class for representing animals in a shelter. 
    """
    def __init__(self, type, name):
      self.type = type
      self.name = name
      self.id = time.strftime("%d%m%M%S")
      self.date = time.strftime("%d/%m/%Y")
      self.adoption = ""

    def setAdopted(self):
      self.adoption = time.strftime("%d/%m/%Y")
      
    
    

