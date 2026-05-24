from funcionarios import *


def main():
    f1 = Funcionario_Mensalista("CArlos", 10000)
    f1.calc_salario()
    f1.analisar_salario()
    f2 = Funcionario_Horista("Maria", 10, 320)
    f2.calc_salario()
    f2.analisar_salario()


if __name__ == "__main__":
    main()
