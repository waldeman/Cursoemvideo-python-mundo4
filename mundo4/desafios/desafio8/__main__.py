from poligono import *
from rich import print


def main():
    q1 = Quadrado(12)
    print(f"Um Quadrado de lado {q1.tamanho_lado} tem perímetro de {q1.perimetro():.1f}m")
    print(f"Um quadraddo de lado {q1.tamanho_lado} tem área de {q1.area():.1f}m²")
    c1 = Circulo(20)
    print(f"Um círculo de raio {c1.tamanho_do_raio} tem perímetro de {c1.perimetro():.1f}m")
    print(f"Um círculo de raio {c1.tamanho_do_raio} tem área de {c1.area():.1f}m²")


if __name__ == "__main__":
    main()
