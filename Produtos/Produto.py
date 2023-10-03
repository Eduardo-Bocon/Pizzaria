from abc import ABC, abstractmethod


class Produto(ABC):

    @abstractmethod
    def __init__(self, preco:float):
        self.preco = preco

    @property
    def preco(self):
        return self.preco

    @preco.setter
    def preco(self, novo_preco):
        self.preco = novo_preco


