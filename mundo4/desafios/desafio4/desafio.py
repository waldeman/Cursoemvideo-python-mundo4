from rich import print
from time import sleep


class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.qnt_paginas = paginas
        self.pag_atual = 1
        print(
            f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.qnt_paginas} páginas[/] no \ntotal. Você agora está na [yellow]página {self.pag_atual}[/][/blue]")

    def avançar_paginas(self, paginas=1):
        cont = 0
        for pag in range(paginas):
            if not self.fim_do_livro():
                self.pag_atual += 1
                print(f"Pag{self.pag_atual} :arrow_forward: ", end=" ", flush=True)
                cont += 1
                sleep(0.3)
        print(f"[blue] Você avançou {cont} páginas e agora está na [yellow]página {self.pag_atual}[/][/blue]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")

    def fim_do_livro(self) -> bool:
        if self.pag_atual == self.qnt_paginas:
            return True
        else:
            return False


l1 = Livro("Dragon Ball Z",20)
l1.avançar_paginas(5)
l1.avançar_paginas(10)
l1.avançar_paginas(7)
l1.avançar_paginas(3)