from random import random, uniform
from fish import Fish

class fishSwarm:
    def objectiveFunction(self, x): 
        return -x**2 + 30*x -10 

    def __init__(self, step, visual, trynumber, fatorLotacao, fishQtd, iteracoes) :
        self.fishs = []

        for _ in range(fishQtd): 
            self.fishs.append(Fish())

        self.step = step
        self.visual = visual
        self.trynumber = trynumber 
        self.fatorLotacao = fatorLotacao
        self.fishQtd = fishQtd 
        self.iteracoes = iteracoes

        print("valores iniciais")
        for fish in self.fishs:
            print(fish.getRepresentation())


    def update(self, Xi, Xj):
        return Xi + (((Xj - Xi)/ abs(Xj - Xi)) * self.step * random())

    def evaluate(self, currentFish): 
        Xmax = self.fishs[0].getRepresentation() 
        summation = 0 
        nf = 0 
        Xi = currentFish.getRepresentation()

        for fish in self.fishs: 
            Xj = fish.getRepresentation() 
            if abs(Xj- Xi) < self.visual: #verifica vizinhança
                nf += 1
                summation += fish.getRepresentation()
                if Xj > Xmax:
                    Xmax = Xj

        Ymax = self.objectiveFunction(Xmax)
        Xc = summation/nf
        Yc = self.objectiveFunction(Xc) 
        Yi = self.objectiveFunction(Xi)

        if nf/self.fishQtd < self.fatorLotacao: #verifica se as redondezas estão lotadas;
            if Ymax > Yi: 
                return self.follow(Xi, Xmax) 
            elif Yc > Yi:
                return self.swarm(Xi, Xc)
        
        return self.prey(Xi)

    def leap(self, Xi):
        return Xi + self.step*random()

    def prey(self, Xi): 
        for _ in range(self.trynumber): 
            Xj = Xi + self.visual*uniform(-1,1) #O peixe escolhe uma posição dentro do seu campo visual
            Yj = self.objectiveFunction(Xj)
            Yi = self.objectiveFunction(Xi)
            if Yj > Yi: 
                return self.update(Xi,Xj) 
        return self.leap(Xi) 

    def follow(self, Xi, Xmax):
       return self.update(Xi, Xmax) 
  
    def swarm(self, Xi, Xc): 
        return self.update(Xi, Xc)

    def execute(self):

        for _ in range(self.iteracoes):
            for i in range(self.fishQtd): 
                aux = self.evaluate(self.fishs[i])
                self.fishs[i].updateRepresentation(aux)
        
        
        print("")
        print("soluções encontradas.")
        for i in range(self.fishQtd):
            print(self.fishs[i].getRepresentation())
        print("")

#step, visual, trynumber, fatorLotacao, fishQtd, iteracoes
fs = fishSwarm(0.3, 5, 10, 0.7, 10, 2000 )
fs.execute()
