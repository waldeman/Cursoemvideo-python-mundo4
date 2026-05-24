from personagens import *


def main():
    g1 = Guerreiro("Kratos", 1000, "soco", "chute", "facada")
    f1 = Mago("Merlim", 1000, "Bola de fogo", "Cajadada", "Estilhaços de gelo")
    g1.atacar(f1, 1000)
    f1.atacar(g1, 1000)
    g1.curar()
    f1.curar()
    g1.atacar(f1, 1000)
    g1.atacar(f1, 1000)


if __name__ == "__main__":
    main()
