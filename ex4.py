import math

class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * (self.raio ** 2)

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

formas = [Circulo(5), Quadrado(4)]

for forma in formas:
    print(forma.area())
