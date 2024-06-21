class Carro:
    def dirigir(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class CarroGasolina(Carro):
    def dirigir(self):
        return "Dirigindo um V8 a gasolina"

class CarroEletrico(Carro):
    def dirigir(self):
        return "Dirigindo um Tesla obiviamente elétrico"

def demonstrar_direcao(carro: Carro):
    print(carro.dirigir())

carros = [CarroGasolina(), CarroEletrico()]

for carro in carros:
    demonstrar_direcao(carro)
