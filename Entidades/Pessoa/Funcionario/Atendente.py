from Entidades.Pessoa.Funcionario.Funcionario import Funcionario


class Atendente(Funcionario):

    def __init__(self):
        super.__init__()
        self.__vendas_mes = 0

    @property
    def vendas_mes(self):
        return self.__vendas_mes
    
    @vendas_mes.setter
    def vendas_mes(self, vendas_mes):
        self.__vendas_mes = vendas_mes