class Garfanhoto:
    """
    Essa Classe cria um garfanhoto, que é uma pessoa que tem nome e idade e pode fazer aniversario.
    para criar uma nova pessoa:
    variavel = Garfanhoto(nome, idade)"""

    def __init__(self, nome="Desconhecido", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Garfanhoto e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"


g1 = Garfanhoto("Ellen", 18)
g1.aniversario()
print(g1.__dict__)
print(g1.__getstate__())
print(g1)
g2 = Garfanhoto("Waldeman", 17)
print(g2)
print(g2.__getstate__())
g3 = Garfanhoto(idade=10)
g3.aniversario()
print(g3)
print(g3.__getstate__())
