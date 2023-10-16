from Entidades.Pessoa.Pessoa import Pessoa
from abc import ABC, abstractmethod


class Funcionario(Pessoa, ABC):

    @abstractmethod
    def __init__(self, nome, cpf, telefone, salario):
        super().__init__(nome, cpf, telefone)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
