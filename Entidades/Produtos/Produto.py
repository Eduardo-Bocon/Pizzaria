from abc import ABC, abstractmethod


class Produto(ABC):

    @abstractmethod
    def __init__(self, preco_venda:float, preco_compra:float, quantidade:int):
        self.__preco_venda = preco_venda
        self.__preco_compra = preco_compra
        self.__quantidade = quantidade

    @property
    def preco_venda(self):
        return self.__preco_venda

    @preco_venda.setter
    def preco_venda(self, novo_preco_venda):
        self.__preco_venda = novo_preco_venda

    @property
    def preco_compra(self):
        return self.__preco_compra

    @preco_compra.setter
    def preco_compra(self, novo_preco_compra):
        self.__preco_compra = novo_preco_compra

    @property
    def quantidade(self):
        return self.__quantidade

    def aumentar_estoque(self, quantidade: int):
        self.__quantidade += quantidade

    def diminuir_estoque(self, quantidade: int):
        self.__quantidade -= quantidade



