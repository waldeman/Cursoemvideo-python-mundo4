from abc import ABC, abstractmethod
from random import randint
from rich import print


class Personagem(ABC):
    def __init__(self, nome, vida, *golpes):
        self.nome: str = nome
        self.vida: int = vida
        self.golpes: list = list(golpes)

    def atacar(self, alvo, forca):
        self.alvo = alvo
        self.forca = forca
        ataque = self.golpes[randint(0, len(self.golpes)-1)]
        print(f"[green]{self.nome}[/]({self.vida}) atacou {self.alvo.nome} com um [blue]{ataque}[/] de força {self.forca}")
        self.alvo.receber_dano(self.forca)

    def receber_dano(self, dano):
        dano_recebido = randint(1, dano)
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {dano_recebido}[/]")
        self.vida -= dano_recebido
        if self.vida > 0:
            print(f"[blue]{self.nome}[/] tem [green]{self.vida} de vida[/] sobrando")
        else:
            print(f"[red]O {self.nome} morreu[/]")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def curar(self):
        cura = randint(1, 100)
        print(f"O [blue]{self.nome}[/] [yellow]enrolou uma atadura nos ferimentos e recuperou[/] [green]{cura} pontos de vida[/]")
        self.vida += cura
        print(f"[blue]{self.nome}[/] agora possui [green]{self.vida} de vida[/]")


class Mago(Personagem):
    def curar(self):
        cura = randint(50, 100)
        print(f"O [blue]{self.nome}[/] usou [yellow]magia de cura e recuperou[/] [green]{cura} pontos de vida[/]")
        self.vida += cura
        print(f"[blue]{self.nome}[/] agora possui [green]{self.vida} de vida[/]")
