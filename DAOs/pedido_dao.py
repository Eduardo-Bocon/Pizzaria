from DAOs.dao import DAO
from Entidades.Pedido import Pedido


class PedidoDAO(DAO):
    def __init__(self):
        super().__init__('pedidos.pkl')

    def add(self, pedido:Pedido):
        if (pedido is not None) and isinstance(pedido, Pedido.Pedido)  and isinstance(pedido.codigo, int):
            super().add(pedido.codigo, pedido)

    def update(self, pedido:Pedido):
        if (pedido is not None) and isinstance(pedido, Pedido.Pedido) and isinstance(pedido.codigo, int):
            super().update(pedido.codigo, pedido)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)