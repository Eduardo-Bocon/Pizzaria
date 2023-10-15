
from Entidades.Pessoa.Funcionario.Atendente import Atendente
from Entidades.Pessoa.Funcionario.Gerente import Gerente
from Entidades.Pessoa.Funcionario.Pizzaiolo import Pizzaiolo
from Entidades.Pessoa.Funcionario.Entregador import Entregador
from Limites.Tela_Funcionario import Tela_Funcionario
from excecoes import Funcionario_ja_cadastrado

class Controlador_Funcionario():

    def __init__(self, controlador_pizzaria):
        self.__lista_Funcionarios = []
        self.__Tela_Funcionario = Tela_Funcionario()
        self.__controlador_pizzaria = controlador_pizzaria

    def cadastrar_funcionario(self):
        dados_funcionario = self.__Tela_Funcionario.pega_dados_funcionario()
        cpf = dados_funcionario["cpf"]
        funcionario = self.busca_funcionario(cpf)

        try:
            if funcionario == None:

                if self.__Tela_Funcionario.escolhe_funcao() == 1:
                    funcionario = Atendente(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["telefone"], dados_funcionario["salario"])
                elif self.__Tela_Funcionario.escolhe_funcao() == 2:
                    funcionario = Gerente(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["telefone"], dados_funcionario["salario"])
                elif self.__Tela_Funcionario.escolhe_funcao() == 3:
                    funcionario = Pizzaiolo(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["telefone"], dados_funcionario["salario"])
                elif self.__Tela_Funcionario.escolhe_funcao() == 4:
                    funcionario = Entregador(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["telefone"], dados_funcionario["salario"])

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
        if self.__lista_Funcionarios is None:
            self.__Tela_Funcionario.mostra_mensagem("Nenhum funcionário cadastrado!")
        
        else:
            for funcionario in self.__lista_Funcionarios:
                if cpf == funcionario.cpf:
                    return funcionario
            self.__Tela_Funcionario.mostra_mensagem("CPF de funcionário não cadastrado!")
    
    def pegar_salarios(self):
        salario = 0
        for funcionario in self.__lista_Funcionarios:
            salario += funcionario.salario
        return salario
    
    def atendente_do_mes(self):
        flag = False
        for funcionario in self.__lista_Funcionarios:
            if isinstance(funcionario, Atendente):
                flag = True

        if flag == False:
            self.__Tela_Funcionario.mostra_mensagem("Nenhum funcionário atendente cadastrado!")

        else:
            vendas_atendente_do_mes = 0

            for funcionario in self.__lista_Funcionarios:
                if isinstance(funcionario, Atendente):
                    if funcionario.vendas_mes > vendas_atendente_do_mes:
                        vendas_atendente_do_mes = funcionario.vendas_mes
                        atendente_do_mes = funcionario

            return atendente_do_mes

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_funcionario, 2: self.modificar_funcionario, 3: self.deletar_funcionario, 4: self.ver_funcionarios, 0: self.retornar}

        while True:
            lista_opcoes[self.__Tela_Funcionario.abre_tela()]()

    def retornar(self):
        self.__controlador_pizzaria.abre_tela_geral()

    def pegar_atendentes(self):
        atendentes = list()
        for funcionario in self.__lista_Funcionarios:
            if isinstance(funcionario, Atendente):
                atendentes.append(funcionario)
        return atendentes
