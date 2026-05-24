from rich import inspect, print
from classes import Aluno, Funcionario, Pessoa, Professor


def main():
    a1 = Aluno("José", 17, "Informática", "3A")
    a1.fazer_aniversario()
    # inspect(a1, methods=True)
    a1.fazer_matricula()
    a1.estudar()
    p1 = Professor("Samuel", 37, "Biologia", "Mestre")
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    f1 = Funcionario("Paulo", 30, "Programador/professor", "Administração")
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()

    # inspect(p1, methods=True)
if __name__ == "__main__":
    main()
