from random import uniform

class Fish:
    def __init__(self, representation = -1):
        self.representation = uniform(0,50)
    
    def updateRepresentation(self, value):
        if value < 0:
            self.representation = 0
        elif value > 50:
            self.representation = 50
        else:
            self.representation = value
    
    def getRepresentation(self):
        return self.representation
