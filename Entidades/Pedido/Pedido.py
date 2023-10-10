from Forma_de_Pagamento import Forma_de_Pagamento

from Entidades.Pessoa.Cliente.Cliente import Cliente
from Entidades.Pessoa.Funcionario.Atendente import Atendente
import datetime


class Pedido:
    
    def __init__(self, cliente: Cliente, atendente: Atendente, valor: float, forma_de_pagamento: Forma_de_Pagamento, data: datetime, entregue: bool, codigo: int):
        self.__cliente = Cliente
        self.__produtos = []
        self.__atendente = Atendente
        self.__valor = valor
        self.__forma_pagamento = Forma_de_Pagamento
        self.__data = datetime
        self.__entregue = entregue
        self.__codigo = codigo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, produtos):
        self.__produtos = produtos

    @property
    def atendente(self):
        return self.__atendente

    @atendente.setter
    def atendente(self, atendente):
        self.__atendente = atendente

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, forma_pagamento):
        self.__forma_pagamento = forma_pagamento

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def entregue(self):
        return self.__entregue

    @entregue.setter
    def entregue(self, entregue):
        self.__entregue = entregue

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    def adicionar_produto(self, produtos):
        pass

    def calcula_preco():
        pass

