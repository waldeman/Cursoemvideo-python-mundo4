from rich import print


class Caneta:
    def __init__(self, cor):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "amarelo":
                escolha = "[yellow]"
            case "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case "rosa":
                escolha = "[pink]"
            case _:
                escolha = "[white]"
        self.tinta = escolha
        self.destampada = False

    def destampar(self) -> bool:
        self.destampada = True

    def escrever(self, texto):
        if self.destampada:
            print(f"{self.tinta} {texto} [/]", end="")
        else:
            print(f":prohibited: A {self.tinta}caneta[/] está tampada")

    def quebrar_linha(self, linhas=1):
        print("\n"*linhas)


c1 = Caneta("vermelho")
c2 = Caneta("amarelo")
c3 = Caneta("Azul")
c1.destampar()
c2.destampar()
c3.destampar()
c1.escrever("Opa")
c2.escrever("Famenfo")
c2.quebrar_linha(1)
c3.escrever("Incrivel")
