class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome: str = nome
        self.idade: int = idade

    def fazer_aniversario(self):
        self.idade += 1
