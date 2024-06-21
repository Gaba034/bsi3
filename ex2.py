class Animal:
    def falar(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class Cachorro(Animal):
    def falar(self):
        return "AAAAAAAAAAAAAUUUUUUUUUUUUUUUUUUUUUUU"

class Gato(Animal):
    def falar(self):
        return "Mewowowoww"

animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())
