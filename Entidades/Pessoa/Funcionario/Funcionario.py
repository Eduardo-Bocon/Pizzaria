from Pessoa.Pessoa import Pessoa
from abc import ABC, abstractmethod


class Funcionario(Pessoa, ABC):

    @abstractmethod
    def __init__(self, salario: float, vendas_mes: int):
        super.__init__()
        self.__salario = salario
        self.__vendas_mes = 0

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def vendas_mes(self):
        return self.__vendas_mes
    
    @vendas_mes.setter
    def vendas_mes(self, vendas_mes):
        self.__vendas_mes = vendas_mes
