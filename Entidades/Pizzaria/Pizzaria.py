from Entidades.Pessoa.Funcionario import Atendente


class Pizzaria:
    def __init__(self):
        self.__receita = 0
        self.__despesas = 0
        self.__total_salarios = 0
        self.__produto_mais_vendido = None
        self.__atendente_do_mes = None

    @property
    def receita(self) -> float:
        return self.__receita
    @receita.setter
    def receita(self, nova_receita):
        if isinstance(nova_receita, float) and nova_receita >= 0:
            self.__receita = nova_receita

    @property
    def despesas(self):
        return self.__despesas

    @despesas.setter
    def despesas(self, nova_despesas):
        if isinstance(nova_despesas, float) and nova_despesas >= 0:
            self.__despesas = nova_despesas

    @property
    def total_salarios(self):
        return self.__total_salarios

    @total_salarios.setter
    def total_salarios(self, novo_total):
        if isinstance(novo_total, float):
            self.__total_salarios = novo_total

    @property
    def produto_mais_vendido(self):
        return self.__produto_mais_vendido

    @produto_mais_vendido.setter
    def produto_mais_vendido(self, novo_produto):
        self.__produto_mais_vendido = novo_produto

    @property
    def atendente_do_mes(self):
        return self.__atendente_do_mes

    @atendente_do_mes.setter
    def atendente_do_mes(self, novo_atendente):
        if isinstance(novo_atendente, Atendente.Atendente):
            self.__atendente_do_mes = novo_atendente