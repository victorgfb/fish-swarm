from random import uniform

class Fish:
    def __init__(self):
        self.representation = uniform(240,256)
    
    def updateRepresentation(self, value):
        if value < 0:
            self.representation = 0
        elif value > 256:
            self.representation = 256
        else:
            self.representation = value
    
    def getRepresentation(self):
        return self.representation
