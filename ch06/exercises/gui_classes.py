class QuestionBlock:
    def __init__(self):
        """
            Initialize the Question block class
        """
        self.containsItem = True #question blocks always start with an item in them
        self.isUsed = False #question blocks always start unused
        self.isProgressive = True #the question block provides a different power-up depending on the size of Mario

class Pipe:
    def __init__(self):
        """
            Initialize the Pipe object class
        """
        self.canEnter = True #this pipe can be entered by the player
        self.color = "green" #this pipe's color is always green
        self.destination = "subareaOne" #this pipe sends Mario to the first sub area

class Goomba:
    def __init__(self):
        """
            Initialize the Goomba enemy class
        """
        self.isAlive = True #the goomba always begins alive
        self.isLoaded = True #the goomba is on screen and can be interacted with
        self.points = 100 #defeating the goomba enemy rewards 100 score points

