from Entidades.Pessoa.Pessoa import Pessoa
from abc import ABC, abstractmethod


class Funcionario(Pessoa, ABC):

    @abstractmethod
    def __init__(self, salario: float, nome:str, cpf:str, telefone:str):
        super().__init__(nome=nome, cpf=cpf, telefone=telefone)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
