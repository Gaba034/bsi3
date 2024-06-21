class Animal:
    def falar(self):
        raise NotImplementedError("Subclasses respondem a esse método")

class Cachorro(Animal):
    def falar(self):
        return "Au au au?"

class Gato(Animal):
    def falar(self):
        return "Meow"

class Peixe(Animal):
    def falar(self):
        return "Blurp blub blop"

animais = [Cachorro(), Gato(), Peixe()]

for animal in animais:
    print(animal.falar())
