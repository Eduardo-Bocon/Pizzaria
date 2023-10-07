from Pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self):
        super.__init__()
        self.__quantidade_pedidos = 0
