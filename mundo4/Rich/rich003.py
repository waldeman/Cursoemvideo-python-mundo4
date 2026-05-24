from rich import print
from rich.table import Table
tabela = Table(title="Tabela de preços" )  
tabela.add_column("Nome", justify="center", style="blue")
tabela.add_column("Preço", justify="center", style="yellow")
tabela.add_row("Lápis", "1,50")
tabela.add_row("Caderno", "20")
tabela.add_row("Mochila", "[white]50[/]")
print(tabela)