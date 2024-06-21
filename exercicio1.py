class Usuario:
    def __init__(self):
        self.pontos = 0
        self.numeroDeArtigos = 0

    def setNumeroDeArtigos(self, nart):
        if isinstance(nart, int) and nart >= 0:
            self.numeroDeArtigos = nart
        else:
            raise ValueError("Tá de brincation with me? Passando número < 0?")

    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos

    def calcPontuacao(self):
        pass

class Autor(Usuario):
    def calcPontuacao(self):
        self.pontos = self.numeroDeArtigos * 10 + 20
        return self.pontos

class Editor(Usuario):
    def calcPontuacao(self):
        self.pontos = self.numeroDeArtigos * 6 + 15
        return self.pontos

autor1 = Autor()
autor1.setNumeroDeArtigos(8123)
print(f"Pontuações do autor: {autor1.calcPontuacao()}")

editor1 = Editor()
editor1.setNumeroDeArtigos(125)
print(f"Pontuações do editor: {editor1.calcPontuacao()}")
