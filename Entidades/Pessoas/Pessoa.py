from abc import ABC, abstractmethod


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome:str, cpf:str, telefone:str):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome

    @property
    def cpf(self):
        return self.cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self.cpf = novo_cpf

    @property
    def telefone(self):
        return self.telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self.telefone = novo_telefone


