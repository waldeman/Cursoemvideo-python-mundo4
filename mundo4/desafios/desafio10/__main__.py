from transportadora import *
from rich.table import Table
from rich import print


def main():
    dist = 50
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    tabela = Table(title="Tabela de fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo", width=10)
    tabela.add_column("Frete", width=20)
    for item in viagem:
        tabela.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.calc_frete()}")
    print(tabela)


if __name__ == "__main__":
    main()
