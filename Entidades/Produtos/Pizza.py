from Entidades.Produtos.Produto import Produto


class Pizza(Produto):
    def __init__(self, nome:str, preco_venda:float, preco_compra:float, quantidade:int):
        super().__init__(nome, preco_venda, preco_compra, quantidade)