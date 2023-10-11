from Tipo_Bebida import Tipo_Bebida
from Produto import Produto


class Bebida(Produto):
    def __init__(self, preco_venda: float, preco_compra: float, quantidade: int, tipo:Tipo_Bebida):
        super.__init__(preco_venda, preco_compra, quantidade)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo_tipo: Tipo_Bebida):
        self.__tipo = novo_tipo