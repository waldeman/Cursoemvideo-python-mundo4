from rich.panel import Panel
from rich import print


class Gamer:
    def __init__(self, nome, nick):
        self.nome_real = nome
        self.nick_name = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)

    def ordem_alfabetica(self):
        return sorted(self.jogos_favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [black on blue] {self.nome_real} [/]\n"
        conteudo += f"Jogos favoritos:\n"
        for i in self.ordem_alfabetica():
            conteudo += f":video_game: [blue]{i}[/]\n"
        ficha = Panel(conteudo, title=f"Jogador <{self.nick_name}>", width=(42))
        print(ficha)


j1 = Gamer("Waldeman Alves", "wamengo")
j1.add_favoritos("God of War")
j1.add_favoritos("Murder Mystery")
j1.add_favoritos("Roblox")
j1.ficha()
j2 = Gamer("Rochele Julios Cris", "GokuAranha244gatinhaspiram")
j2.add_favoritos("Bob Sponja Simulator")
j2.add_favoritos("Mario Kart")
j2.add_favoritos("Goat Simulator")
j2.ficha()
