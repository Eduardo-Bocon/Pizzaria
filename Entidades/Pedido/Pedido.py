from Forma_de_Pagamento import Forma_de_Pagamento
from Entidades.Pessoa.Cliente import Cliente
from Entidades.Pessoa.Funcionario.Atendente import Atendente
import datetime


class Pedido:
    
    def __init__(self, cliente, produtos, atendente, valor: float, forma_pagamento, data, entregue: bool, codigo: int):
        self.__cliente = Cliente
        self.__produtos = []
        self.__atendente = Atendente
        self.__valor = valor
        self.__forma_pagamento = Forma_de_Pagamento
        self.__data = datetime
        self.__entregue = entregue
        self.__codigo = codigo

    def adicionar_produto(self, produtos):
        pass

    def calcula_preco():
        pass