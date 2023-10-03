from abc import ABC, abstractmethod


class Produto(ABC):

    @abstractmethod
    def __init__(self, preco:float):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco


