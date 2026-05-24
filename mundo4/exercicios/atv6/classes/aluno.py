from classes.pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso: str = curso
        self.turma: str = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} foi matrículado")