from Estoque.Estoque import Estoque
from Produtos.Produto import Produto
from Produtos.Tipo_Bebida import Tipo_Bebida


class Bebida (Produto):
    def __init__(self, preco:float, tipo:Tipo_Bebida):
        self.__tipo = tipo
        super().__init__(preco)

    def tem_estoque(self, estoque:Estoque):
        if estoque.self.__tipo.name > 0:
            return True
        return False