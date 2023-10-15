from Entidades.Produto.Produto import Produto

class Pizza(Produto):
    def __init__(self, preco_venda:float, preco_compra:float, quantidade:int, sabor: str):
        super.__init__(preco_venda, preco_compra, quantidade)
        self.__sabor = sabor

    @property
    def sabor(self):
        return self.__sabor

    @sabor.setter
    def sabor(self, novo_sabor: str):
        self.__sabor = novo_sabor