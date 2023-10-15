from Controladores.Controlador_Funcionario import Controlador_Funcionario
from Controladores.Controlador_Pedido import Controlador_Pedido
from Controladores.Controlador_Produto import Controlador_Produto
from Controladores.Controlador_Cliente import Controlador_Cliente
from Limites.Tela_Pizzaria import Tela_Pizzaria


class Controlador_Pizzaria(): #todo

    def __init__(self):
        self.__contr_produto = Controlador_Produto()
        self.__contr_pedido = Controlador_Pedido()
        self.__contr_funcionario = Controlador_Funcionario()
        self.__contr_cliente = Controlador_Cliente()
        self.__tela_pizzaria = Tela_Pizzaria()

    def calcular_receitas(self):
        pass

    def calcular_despesas(self):
        pass

    def calcular_total_salarios(self):
        self.__contr_funcionario.pegar_salarios()

    def produto_mais_vendido(self):
        pass

    def atendente_do_mes(self):
        self.__contr_funcionario.atendente_do_mes()

    def abre_tela(self):
        lista_opcoes = {1: self.__contr_produto.abre_tela(), 2: self.__contr_cliente.abre_tela(), 3: self.__contr_funcionario.abre_tela(), 4: self.__contr_pedido.abre_tela(), 5: self.__tela_pizzaria.ver_relatorio(self.calcular_total_salarios(), self.calcular_despesas(), self.calcular_receitas(), self.atendente_do_mes()), 0: self.encerra_sistema}

        while True:
            lista_opcoes[self.__tela_pizzaria.abre_tela()]()

    def encerra_sistema(self):
        exit(0)
