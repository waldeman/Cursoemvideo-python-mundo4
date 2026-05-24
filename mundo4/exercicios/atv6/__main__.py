from rich import inspect, print
from classes.pessoa import Pessoa
from classes.aluno import Aluno
from classes.professor import Professor
from classes.funcionario import Funcionario


def main():
    a1 = Aluno("José", 17, "Informática", "3A")
    a1.fazer_aniversario()
    # inspect(a1, methods=True)
    a1.fazer_matricula()
    p1 = Professor("Samuel", 37, "Biologia", "Mestre")
    p1.fazer_aniversario()
    p1.dar_aula()
    f1 = Funcionario("Paulo", 30, "Programador/professor", "Administração")
    f1.fazer_aniversario()
    f1.bater_ponto()

    # inspect(p1, methods=True)
if __name__ == "__main__":
    main()
