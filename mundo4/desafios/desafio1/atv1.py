from rich import print
from rich import inspect


class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}"

Funcionario.empresa = "Hostnet"
c1 = Funcionario("Waldeman", "TI", "Programador")
print(c1.apresentacao())
c2 = Funcionario("Ellen", "Minha vida", "Dona da minha existência")
print(c2.apresentacao())
