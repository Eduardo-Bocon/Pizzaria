from Entidades.Pedido.Forma_de_Pagamento import Forma_de_Pagamento
from Entidades.Pessoa.Cliente.Cliente import Cliente
from Entidades.Pessoa.Funcionario.Atendente import Atendente
import datetime


class Pedido:
    
    def __init__(self, produtos:list(),cliente: Cliente, atendente: Atendente, forma_de_pagamento: Forma_de_Pagamento, data: datetime, codigo: int):
        self.__cliente = cliente
        self.__produtos = produtos
        self.__atendente = atendente
        self.__forma_pagamento = forma_de_pagamento
        self.__data = data
        self.__codigo = codigo
        self.__entregue = False

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
    def entregue(self, entregue:bool):
        self.__entregue = entregue

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def calcula_preco(self):
        preco = 0
        for produto in self.__produtos:
            preco += produto.preco_venda

        return preco

    def calcula_gastos(self):
        gastos = 0
        for produto in self.__produtos:
            gastos += produto.preco_compra

        return gastos
