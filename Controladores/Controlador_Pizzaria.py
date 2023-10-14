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

    def pegar_lucro(self):
        pass

    def calcular_receitas(self):
        pass

    def calcular_despesas(self):
        despesa_salario = self.__contr_funcionario.pegar_salarios()

    def calcular_total_salarios(self):
        self.__contr_funcionario.pegar_salarios()

    def abre_tela(self):
        lista_opcoes = {1: self.pegar_lucro, 2: self.calcular_receitas, 3: self.calcular_despesas, 4: self.calcular_total_salarios, 0: self.encerra_sistema}

        while True:
            lista_opcoes[self.__tela_pizzaria.abre_tela()]()

    def encerra_sistema(self):
        exit(0)
