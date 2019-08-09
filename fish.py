from random import uniform

class Fish:
    def __init__(self, representation = -1):
        self.representation = uniform(0,31)
    
    def updateRepresentation(self, value):
        if value < 0:
            self.representation = 0
        elif value > 31:
            self.representation = 31
        else:
            self.representation = value
    
    def getRepresentation(self):
        return self.representation
