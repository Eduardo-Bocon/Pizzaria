from Limites.Tela_Pedido import Tela_Pedido
from Entidades.Pedido.Pedido import Pedido


class Controlador_Pedido():  # todo

    def __init__(self):
        self.__lista_pedidos = []
        self.__tela = Tela_Pedido()

    def fazer_pedido(self, pedido: Pedido):
        pass

    def deletar_pedido(self, codigo:str):

        self.ver_pedidos()
        nome = self.__tela.escolher_pedido()
        pedido = self.pegar_pedido(codigo)

        if pedido is not None:
            self.__lista_pedidos.remove(pedido)
            self.ver_pedidos()
        else:
            self.__tela.mostra_mensagem("Erro: pedido não existente")

    def modificar_pedido(self, pedido: Pedido):
        pass

    def pegar_pedido(self, codigo):
        pass

    def ver_pedidos(self, cliente=None):
        pass

    def abre_tela(self):
        pass

    def retornar(self):
        pass
