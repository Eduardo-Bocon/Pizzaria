from Pessoa import Pessoa
from Entidades.Pessoa.Cliente.Endereco import Endereco


class Cliente(Pessoa):

    def __init__(self):
        super.__init__()
        self.__quantidade_pedidos = 0
        self.__endereco = Endereco

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
