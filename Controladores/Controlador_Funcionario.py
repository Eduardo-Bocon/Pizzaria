
from Entidades.Pessoa.Funcionario.Funcionario import Funcionario
from Limites.Tela_Funcionario import Tela_Funcionario
from Controladores import Controlador_Pizzaria
from excecoes import Funcionario_ja_cadastrado

class Controlador_Funcionario():

    def __init__(self, controlador_pizzaria: Controlador_Pizzaria):
        self.__lista_Funcionarios = []
        self.__Tela_Funcionario = Tela_Funcionario()
        self.__controlador_pizzaria = controlador_pizzaria

    def cadastrar_funcionario(self):
        dados_funcionario = self.__Tela_Funcionario.pega_dados_funcionario()
        cpf = dados_funcionario["cpf"]
        funcionario = self.busca_funcionario(cpf)

        try:
            if funcionario == None:
                ###############################################ERRO
                funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["telefone"], dados_funcionario["salario"])
                self.__lista_Funcionarios.append(funcionario)
                self.__Tela_Funcionario.mostra_mensagem("Cadastro de funcionário realizado!")

            else:
                raise Funcionario_ja_cadastrado(funcionario)
        except Funcionario_ja_cadastrado as e:
            self.__Tela_Funcionario.mostra_mensagem(e)

    def deletar_funcionario(self):
        self.ver_funcionarios()
        busca_funcionario = self.__Tela_Funcionario.seleciona_funcionario()
        funcionario = self.busca_funcionario(busca_funcionario)

        if funcionario is not None:
            self.__lista_Funcionarios.remove(funcionario)
            self.__Tela_Funcionario.mostra_mensagem("Remoção de cadastro de funcionário realizado!")
            self.ver_funcionarios()

        else:
            self.__Tela_Funcionario.mostra_mensagem("Funcionário não cadastrado!")

    def modificar_funcionario(self):
        self.ver_funcionarios()
        busca_funcionario = self.__Tela_Funcionario.seleciona_funcionario()
        funcionario = self.busca_funcionario(busca_funcionario)

        if funcionario is not None:
            novos_dados_funcionario = self.__Tela_Funcionario.pega_dados_funcionario()

            funcionario.nome = novos_dados_funcionario["nome"]
            funcionario.cpf = novos_dados_funcionario["cpf"]
            funcionario.telefone = novos_dados_funcionario["telefone"]
            funcionario.salario = novos_dados_funcionario["salario"]

            self.ver_funcionarios()
            self.__Tela_Funcionario.mostra_mensagem("Modificação de cadastro de funcionário realizado!")
        
        else:
            self.__Tela_Funcionario.mostra_mensagem("Funcionário não cadastrado!")

    def ver_funcionarios(self):
        if self.__lista_Funcionarios == None:
            self.__Tela_Funcionario.mostra_mensagem("Nenhum Atendente cadastrado!")

        else:
            for funcionario in self.__lista_Funcionarios:
                self.__Tela_Funcionario.mostra_funcionarios({"nome": funcionario.nome, "cpf": funcionario.cpf, "telefone": funcionario.telefone, "salario": funcionario.salario})

    def busca_funcionario(self, cpf: str):
        for funcionario in self.__lista_Funcionarios:
            if cpf == funcionario.cpf:
                return funcionario
        return None
    
    def pegar_salarios(self):
        salario = 0
        for funcionario in self.__lista_Funcionarios:
            salario += funcionario.salario
        return salario

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_funcionario, 2: self.modificar_funcionario, 3: self.deletar_funcionario, 4: self.ver_funcionarios, 0: self.retornar}

        while True:
            lista_opcoes[self.__Tela_Funcionario.tela_opcoes()]()

    def retornar(self):
        self.__controlador_pizzaria.tela_geral()
