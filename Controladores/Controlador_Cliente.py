from Limites.Tela_Cliente import Tela_Cliente
from Entidades.Pessoa.Cliente.Cliente import Cliente

class Controlador_CLiente():

    def __init__(self, Controlador_Pizzaria):
        self.__lista_Clientes = []
        self.__tela_Cliente = Tela_Cliente()
        self.__Controlador_Pizzaria = Controlador_Pizzaria

    def cadastrar_cliente(self, cliente: Cliente):
        pass
    
    def deletar_cliente(self, cliente: Cliente):
        pass
    
    def modificar_cliente(self, cliente: Cliente):
        pass

    def ver_cliente():
        pass

    def ver_clientes_fieis():
        pass
