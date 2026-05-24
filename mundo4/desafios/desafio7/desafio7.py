from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()


class Controle_remoto:
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal=1, vol=2):
        self.canal = canal
        self.volume = vol
        self.ligada = False

    def mostrar_tv(self):
        while True:
            console.clear()
            if not self.ligada:
                conteudo = f":prohibited: [red]A tv está desligada[/]"
            else:
                conteudo = f"Canal  = "
                for canal in range(Controle_remoto.canal_min, Controle_remoto.canal_max + 1):
                    if canal == self.canal:
                        conteudo += f"[yellow on yellow] {canal} [/]"
                    else:
                        conteudo += f" {canal} "
                conteudo += f"\nVolume = "
                for volume in range(Controle_remoto.volume_min, Controle_remoto.volume_max):
                    if volume <= self.volume:
                        conteudo += f"[on green]  [/]"
                    else:
                        conteudo += f"[on white]  [/]"
            tela = Panel(conteudo, title="[ Tv ]", width=30)
            print(tela)
            controle = input(f"< CH{self.canal} >   - VOl{self.volume} + ")
            if controle == "@":
                self.ligar_desligar_tv()
            if self.ligada:
                if controle == "0":
                    break
                elif controle == "<":

                    if self.canal > Controle_remoto.canal_min:
                        self.canal -= 1
                    else:
                        self.canal = self.canal_max
                elif controle == ">":
                    if self.canal < Controle_remoto.canal_max:
                        self.canal += 1
                    else:
                        self.canal = Controle_remoto.canal_min
                elif controle == "+":
                    if self.volume < Controle_remoto.volume_max:
                        self.volume += 1
                elif controle == "-":
                    if self.volume > Controle_remoto.volume_min:
                        self.volume -= 1

    def ligar_desligar_tv(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


tv1 = Controle_remoto()
tv1.mostrar_tv()
