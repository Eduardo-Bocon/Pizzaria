from Controladores.Controlador_Funcionario import Controlador_Funcionario
from Controladores.Controlador_Pedido import Controlador_Pedido
from Controladores.Controlador_Produto import Controlador_Produto
from Controladores.Controlador_Cliente import Controlador_Cliente
from Entidades.Pizzaria.Pizzaria import Pizzaria
from Limites.Tela_Pizzaria import Tela_Pizzaria
from Limites.Tela_Geral import Tela_Geral


class Controlador_Pizzaria():

    def __init__(self):
        self.__contr_produto = Controlador_Produto(self)
        self.__contr_pedido = Controlador_Pedido(self)
        self.__contr_funcionario = Controlador_Funcionario(self)
        self.__contr_cliente = Controlador_Cliente(self)
        self.__tela_pizzaria = Tela_Pizzaria()
        self.__tela_geral = Tela_Geral()
        self.__pizzaria = Pizzaria()

    def inicializa_sistema(self):
        self.abre_tela_geral()

    def mostrar_financeiro(self):
        self.__tela_pizzaria.mostrar_financeiro(salarios=self.pegar_salarios(), despesas=self.pegar_despesas(), receitas=self.pegar_receitas())

    def pegar_salarios(self):
        salarios = self.__contr_funcionario.pegar_salarios()
        self.__pizzaria.total_salarios = salarios
        return salarios

    def pegar_despesas(self):
        despesas = self.__contr_pedido.pegar_despesas()
        self.__pizzaria.despesas = despesas
        return despesas

    def pegar_receitas(self):
        receitas = self.__contr_pedido.pegar_receitas()
        self.__pizzaria.receita = receitas
        return receitas

    def produto_mais_vendido(self):
        produto = self.__contr_pedido.pegar_produto_mais_vendido()
        self.__tela_pizzaria.produto_mais_vendido(produto)
        self.__pizzaria.produto_mais_vendido = produto

    def atendente_do_mes(self):
        atendente = self.__contr_funcionario.atendente_do_mes()
        self.__tela_pizzaria.atendente_do_mes(atendente)
        self.__pizzaria.atendente_do_mes = atendente

    def abre_tela_geral(self):
        lista_opcoes = {1: self.__contr_produto.abre_tela, 2: self.__contr_cliente.abre_tela,
                        3: self.__contr_funcionario.abre_tela, 4: self.__contr_pedido.abre_tela,
                        5: self.abre_tela, 0: self.encerra_sistema}

        while True:
            lista_opcoes[self.__tela_geral.abre_tela_geral()]()

    def abre_tela(self):

        lista_opcoes = {1: self.atendente_do_mes,
                        2: self.produto_mais_vendido,
                        3: self.mostrar_financeiro,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_pizzaria.abre_tela()]()

    def retornar(self):
        self.abre_tela_geral()

    def encerra_sistema(self):
        exit(0)

    def pegar_atendentes(self):
        return self.__contr_funcionario.pegar_atendentes()

    def pegar_pizzas(self):
        return self.__contr_produto.pegar_pizzas()

    def pegar_bebidas(self):
        return self.__contr_produto.pegar_bebidas()

    def pegar_cliente_por_cpf(self, cpf):
        self.__contr_cliente.busca_clientes(cpf)
