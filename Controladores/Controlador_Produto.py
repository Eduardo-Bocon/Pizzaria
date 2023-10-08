from Controladores import Controlador_Pizzaria
from Telas.Tela_Produto import Tela_Produto

class Controlador_Produto():

    def __init__(self, controlador_pizzaria:Controlador_Pizzaria):
        self.__tela = Tela_Produto()
        self.__controlador_pizzaria = controlador_pizzaria
        self.__produtos = []

    def retornar(self):
        self.__controlador_pizzaria.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_produto, 2: self.modificar_produto, 3: self.deletar_produto, 4: self.ver_produtos,
                        0: self.retornar}

        while 1:
            lista_opcoes[self.__tela.tela_opcoes()]()

    def cadastrar_produto(self):
        pass

    def modificar_produto(self):
        pass

    def deletar_produto(self):
        pass

    def ver_produtos(self):
        pass