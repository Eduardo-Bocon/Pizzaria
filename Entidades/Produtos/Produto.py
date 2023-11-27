from abc import ABC, abstractmethod


class Produto(ABC):

    @abstractmethod
    def __init__(self, nome:str, preco_venda:float, preco_compra:float, quantidade:int):
        self.__nome = nome
        self.__preco_venda = preco_venda
        self.__preco_compra = preco_compra
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome is not None:
            self.__nome = novo_nome

    @property
    def preco_venda(self):
        return self.__preco_venda

    @preco_venda.setter
    def preco_venda(self, novo_preco_venda):
        if isinstance(novo_preco_venda, float) and novo_preco_venda >= 0:
            self.__preco_venda = novo_preco_venda

    @property
    def preco_compra(self):
        return self.__preco_compra

    @preco_compra.setter
    def preco_compra(self, novo_preco_compra):
        if isinstance(novo_preco_compra, float) and novo_preco_compra >= 0:
            self.__preco_compra = novo_preco_compra

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self.__quantidade = nova_quantidade

    def aumentar_estoque(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade += quantidade

    def diminuir_estoque(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade -= quantidade
