from abc import ABC, abstractmethod


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome:str, cpf:str, telefone:str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if isinstance(novo_cpf, str):
            self.__cpf = novo_cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if isinstance(novo_telefone, str):
            self.__telefone = novo_telefone
