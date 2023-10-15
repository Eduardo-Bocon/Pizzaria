
from Entidades.Pessoa.Funcionario.Funcionario import Funcionario
from Limites.Tela_Funcionario import Tela_Funcionario

class Controlador_Funcionario(): #todo

    def __init__(self):
        self.__lista_Atendentes = []
        self.__lista_Outros_Funcionarios = []
        self.__Tela_Funcionario = Tela_Funcionario()

    def cadastrar_funcionario(self, funcionario: Funcionario):
        pass

    def deletar_funcionario(self, funcionario: Funcionario):
        pass

    def modificar_funcionario(self, funcionario: Funcionario):
        pass

    def ver_funcionario(self):
        pass

    def abre_tela(self):
        pass

    def retornar(self):
        pass

    def pegar_salarios(self) -> float:
        salarios = 0
        for funcionario in self.__lista_Atendentes:
            salarios += funcionario.salario
        for funcionario in self.__lista_Outros_Funcionarios:
            salarios += funcionario.salario
        return salarios

