from Controladores.Controlador_Funcionario import Controlador_Funcionario
from Controladores.Controlador_Pedido import Controlador_Pedido
from Controladores.Controlador_Produto import Controlador_Produto
from Controladores.Controlador_Cliente import Controlador_Cliente


class Controlador_Pizzaria: #todo

    def __init__(self):
        self.__contr_produto = Controlador_Produto()
        self.__contr_pedido = Controlador_Pedido()
        self.__contr_funcionario = Controlador_Funcionario()
        self.__contr_cliente = Controlador_Cliente()

    def pegar_lucro(self):
        pass

    def calcular_receitas(self):
        pass

    def calcular_despesas(self):
        pass

    def calcular_total_salarios(self) -> float:
        pass