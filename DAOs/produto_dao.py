from DAOs.dao import DAO
from Entidades.Produtos import Pizza, Bebida


class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto):
        if produto is not None and (isinstance(produto, Pizza.Pizza) or isinstance(produto, Bebida.Bebida)) and isinstance(
                produto.nome, str):
            super().add(produto.nome, produto)

    def update(self, produto):
        if produto is not None and (isinstance(produto, Pizza.Pizza) or isinstance(produto, Bebida.Bebida)) and isinstance(
                produto.nome, str):
            super().update(produto.nome, produto)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
