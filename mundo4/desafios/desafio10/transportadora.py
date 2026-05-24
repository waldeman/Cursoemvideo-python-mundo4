from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia: float = distancia
        self.valor_frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    valor_por_km = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        return f"R${Moto.valor_por_km * self.distancia:,.2f}"


class Caminhao(Transporte):
    valor_por_km = 1.20
    distancia_min = 50.0

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.verficar_distancia():
            return f"R${Caminhao.valor_por_km * self.distancia:,.2f}"
        else:
            return ("Raio mínimo de 50 km")

    def verficar_distancia(self):
        if self.distancia >= Caminhao.distancia_min:
            return True
        else:
            return False


class Drone(Transporte):
    valor_por_km = 9.50
    distancia_max = 10.0

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.verficar_distancia():
            return f"R${Drone.valor_por_km * self.distancia:,.2f}"
        else:
            return ("Raio máximo de 10 km")

    def verficar_distancia(self):
        if self.distancia <= Drone.distancia_max:
            return True
        else:
            return False
