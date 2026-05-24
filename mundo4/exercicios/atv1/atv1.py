class Garfanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Garfanhoto e tem {self.idade} anos de idade"


g1 = Garfanhoto()
g1.nome = "Ellen"
g1.idade = 18
g1.aniversario()
print(g1.mensagem())

g2 = Garfanhoto()
g2.nome = "Waldeman"
g2.idade = 17
print(g2.mensagem())
g3 = Garfanhoto()
g3.nome = "n fsab"
g3.aniversario() 
print(g3.mensagem())