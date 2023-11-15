from Entidades.Produtos.Produto import Produto

class Bebida(Produto):
    def __init__(self, preco_venda: float, preco_compra: float, quantidade: int, nome:str):
        super().__init__(nome, preco_venda, preco_compra, quantidade)



