from Entidades.Pessoa.Funcionario.Funcionario import Funcionario


class Atendente(Funcionario):

    def __init__(self, salario: float, nome: str, cpf: str, telefone: str):
        super().__init__(salario=salario, nome=nome, cpf=cpf, telefone=telefone)
        self.__vendas_mes = 0

    @property
    def vendas_mes(self):
        return self.__vendas_mes
    
    @vendas_mes.setter
    def vendas_mes(self, vendas_mes):
        self.__vendas_mes = vendas_mes