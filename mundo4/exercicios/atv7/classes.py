from abc import ABC,  abstractmethod


class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome: str = nome
        self.idade: int = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso: str = curso
        self.turma: str = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} foi matrículado")

    def estudar(self):
        print(f"O aluno {self.nome} está estudando {self.curso} na turma {self.turma}")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} iniciou a aula de {self.especialidade}")

    def estudar(self):
        print(f"O professor {self.nome} é {self.nivel} em {self.especialidade}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário {self.nome} bateu o ponto ")

    def estudar(self):
        print(f"O funcionario {self.nome} é {self.cargo} e se especializa para {self.setor}")
