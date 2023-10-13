from Limites.Tela_Pedido import Tela_Pedido
from Entidades.Pedido.Pedido import Pedido
from Controladores import Controlador_Pizzaria


class Controlador_Pedidos():

    def __init__(self, controlador_pizzaria: Controlador_Pizzaria):
        self.__lista_pedidos = []
        self.__Tela_Pedido = Tela_Pedido()
        self.__Controlador_Pizzaria = controlador_pizzaria

    def fazer_pedido(self, pedido: Pedido):
        pass
    
    def deletar_pedido(self, pedido: Pedido):
        pass
    
    def modificar_pedido(self, pedido: Pedido):
        pass

    def ver_pedido():
        pass

    def abre_tela():
        pass

    def retornar():
        pass
