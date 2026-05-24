from rich import print
from rich.panel import Panel


class Churrasco():
    consumo = 0.400
    preco = 82.40

    def __init__(self, nome, qnt_pessoas):
        self.nome = nome
        self.quantidade_de_pessoas = qnt_pessoas

    def calcular_qnt_carne(self):
        qnt_carne = self.quantidade_de_pessoas * self.consumo
        return qnt_carne

    def calcular_preco_total(self):
        qnt_total = self.calcular_qnt_carne() * Churrasco.preco
        return qnt_total

    def calcular_preco_por_pessoa(self):
        preco_pessoa = self.calcular_preco_total()/self.quantidade_de_pessoas
        return preco_pessoa

    def analisar(self):
        conteudo = f"Analisando [green]{self.nome}[/] com [blue]{self.quantidade_de_pessoas}[/] convidados\n"
        conteudo += f"Cada participante comerá {Churrasco.consumo:,.1f}Kg e cada Kg custa R${Churrasco.preco:,.2f}\n"
        conteudo += f"Recomendo [blue]comprar {self.calcular_qnt_carne():,.3f}kg[/] de carne\n"
        conteudo += f"O custo total será de [green]R${self.calcular_preco_total():,.2f}[/]\n"
        conteudo += f"Cada pessoa pagará [yellow]R${self.calcular_preco_por_pessoa():,.2f}[/] por pessoa"
        analise = Panel(conteudo, title=self.nome, width=70)
        print(analise)


c1 = Churrasco("Churrasco de família", 10)
c1.analisar()
c2 = Churrasco("Churras dos Amigos", 15)
c2.analisar()
c3 = Churrasco("Festa da cidade", 100)
c3.analisar()
