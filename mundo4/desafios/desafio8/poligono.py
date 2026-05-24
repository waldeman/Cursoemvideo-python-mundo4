from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(4)
        self.tamanho_lado = lado

    def perimetro(self):
        perimetro = self.tamanho_lado * self.qtd_lados
        return perimetro

    def area(self):
        area = self.tamanho_lado ** 2
        return area


class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(0)
        self.tamanho_do_raio = raio

    def perimetro(self):
        perimetro = 2 * 3.14 * self.tamanho_do_raio
        return perimetro

    def area(self):
        area = 3.14 * self.tamanho_do_raio ** 2
        return area
