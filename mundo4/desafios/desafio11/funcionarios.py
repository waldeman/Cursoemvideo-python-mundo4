from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    salario_min = 1621
    inss = 7.5
    tipo = ""

    def __init__(self, nome):
        self.nome: str = nome
        self.salario_bruto = 0
        self.salario = 0
        self.salarios_min = 0

    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        conteudo = f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de "
        conteudo += f"[green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salarios_min:.1f} salários mínimos[/]."
        painel = Panel(conteudo, title="Análise de Salário", width=50)
        print(painel)


class Funcionario_Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome)
        self.valor_hora: float = valor_hora
        self.horas_trabalhadas: int = horas_trabalhadas

    def calc_salario(self):
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario_Horista.inss / 100)
        self.salarios_min = self.salario/Funcionario_Horista.salario_min


class Funcionario_Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.salario_bruto: float = sal_bruto

    def calc_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario_Mensalista.inss / 100)
        self.salarios_min = self.salario/Funcionario_Mensalista.salario_min
