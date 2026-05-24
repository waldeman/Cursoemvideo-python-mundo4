from rich import print
from rich.panel import Panel


class Produto():
    produto = "Produto"

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = f"R${preco:,.2f}"

    def etiqueta(self):
        conteudo = f"{self.nome.center(38)}"
        conteudo += f"{"-"*38}"
        conteudo += f"{self.preco.center(38, ".")}"
        painel = Panel(conteudo, title=Produto.produto, width=42)

        print(painel)


c1 = Produto("Cadeira", 50)
c1.etiqueta()
c2 = Produto("Pc Gamer", 5_000)
c2.etiqueta()
c3 = Produto("Iphone 17 Pro Max", 25_000.96)
c3.etiqueta()
