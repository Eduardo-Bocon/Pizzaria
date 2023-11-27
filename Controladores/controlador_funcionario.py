from DAOs.funcionario_dao import FuncionarioDAO
from Entidades.Pessoa.Funcionario.Atendente import Atendente
from Entidades.Pessoa.Funcionario.Gerente import Gerente
from Entidades.Pessoa.Funcionario.Pizzaiolo import Pizzaiolo
from Entidades.Pessoa.Funcionario.Entregador import Entregador
from Limites.Tela_Funcionario import Tela_Funcionario
from excecoes import Funcionario_ja_cadastrado


class ControladorFuncionario():

    def __init__(self, controlador_pizzaria):
        self.__funcionario_DAO = FuncionarioDAO()
        self.__Tela_Funcionario = Tela_Funcionario()
        self.__controlador_pizzaria = controlador_pizzaria

    def cadastrar_funcionario(self):
        dados_funcionario = self.__Tela_Funcionario.pega_dados_funcionario()
        cpf = dados_funcionario["cpf"]
        funcionario = self.busca_funcionario(cpf, True)

        try:
            if funcionario is None:

                funcao = self.__Tela_Funcionario.escolhe_funcao()

                if funcao == "1":
                    funcionario = Atendente(nome=dados_funcionario["nome"], cpf=dados_funcionario["cpf"],
                                            telefone=dados_funcionario["telefone"],
                                            salario=dados_funcionario["salario"])
                elif funcao == "2":
                    funcionario = Gerente(nome=dados_funcionario["nome"], cpf=dados_funcionario["cpf"],
                                          telefone=dados_funcionario["telefone"], salario=dados_funcionario["salario"])
                elif funcao == "3":
                    funcionario = Pizzaiolo(nome=dados_funcionario["nome"], cpf=dados_funcionario["cpf"],
                                            telefone=dados_funcionario["telefone"],
                                            salario=dados_funcionario["salario"])
                elif funcao == "4":
                    funcionario = Entregador(nome=dados_funcionario["nome"], cpf=dados_funcionario["cpf"],
                                             telefone=dados_funcionario["telefone"],
                                             salario=dados_funcionario["salario"])
                self.__funcionario_DAO.add(funcionario)
                self.__Tela_Funcionario.mostra_mensagem("Cadastro de funcionário realizado!")

            else:
                raise Funcionario_ja_cadastrado(funcionario)
        except Funcionario_ja_cadastrado as e:
            self.__Tela_Funcionario.mostra_mensagem(e)

    def deletar_funcionario(self):
        self.ver_funcionarios()

        if not self.__funcionario_DAO.get_all():
            self.__Tela_Funcionario.mostra_mensagem("Nenhum funcionário cadastrado!")
        
        else:
            busca_funcionario = self.__Tela_Funcionario.seleciona_funcionario()
            funcionario = self.busca_funcionario(busca_funcionario, True)

            if funcionario is not None:
                self.__funcionario_DAO.remove(funcionario.cpf)
                self.__Tela_Funcionario.mostra_mensagem("Remoção de cadastro de funcionário realizado!")
                self.ver_funcionarios()

            else:
                self.__Tela_Funcionario.mostra_mensagem("Funcionário não cadastrado!")

    def modificar_funcionario(self):
        self.ver_funcionarios()

        if not self.__funcionario_DAO.get_all():
            self.__Tela_Funcionario.mostra_mensagem("Nenhum funcionário cadastrado!")
        
        else:
            busca_funcionario = self.__Tela_Funcionario.seleciona_funcionario()
            funcionario = self.busca_funcionario(busca_funcionario, True)

            if funcionario is not None:
                novos_dados_funcionario = self.__Tela_Funcionario.pega_dados_funcionario({"nome":funcionario.nome, "cpf":funcionario.cpf, "telefone":funcionario.telefone, "salario":funcionario.salario})

                funcionario.nome = novos_dados_funcionario["nome"]
                funcionario.cpf = novos_dados_funcionario["cpf"]
                funcionario.telefone = novos_dados_funcionario["telefone"]
                funcionario.salario = novos_dados_funcionario["salario"]

                self.__funcionario_DAO.update(funcionario)

                self.ver_funcionarios()
                self.__Tela_Funcionario.mostra_mensagem("Modificação de cadastro de funcionário realizado!")

            else:
                self.__Tela_Funcionario.mostra_mensagem("Funcionário não cadastrado!")

    def ver_funcionarios(self):
        if not self.__funcionario_DAO.get_all():
            self.__Tela_Funcionario.mostra_mensagem("Nenhum funcionário cadastrado!")

        else:
            lista_funcionarios = []
            for funcionario in self.__funcionario_DAO.get_all():
                lista_funcionarios.append({"nome": funcionario.nome, "cpf": funcionario.cpf, "telefone": funcionario.telefone,
                     "salario": funcionario.salario})
            self.__Tela_Funcionario.mostra_funcionarios(lista_funcionarios)

    def busca_funcionario(self, cpf: str, silenciosa:bool):

        if not self.__funcionario_DAO.get_all():
            if not silenciosa:
                self.__Tela_Funcionario.mostra_mensagem("Nenhum funcionário cadastrado!")
            return None

        else:
            for funcionario in self.__funcionario_DAO.get_all():
                if cpf == funcionario.cpf:
                    return funcionario
            if not silenciosa:
                self.__Tela_Funcionario.mostra_mensagem("CPF de funcionário não cadastrado!")

    def pegar_salarios(self):
        salario = 0
        for funcionario in self.__funcionario_DAO.get_all():
            salario += float(funcionario.salario)
        return salario

    def atendente_do_mes(self):
        atendente_do_mes = None
        flag = False
        for funcionario in self.__funcionario_DAO.get_all():
            if isinstance(funcionario, Atendente):
                flag = True

        if not flag:
            self.__Tela_Funcionario.mostra_mensagem("Nenhum funcionário atendente cadastrado!")

        else:
            vendas_atendente_do_mes = 0

            for funcionario in self.__funcionario_DAO.get_all():
                if isinstance(funcionario, Atendente):
                    print(funcionario.vendas_mes)
                    if funcionario.vendas_mes > vendas_atendente_do_mes:
                        vendas_atendente_do_mes = funcionario.vendas_mes
                        atendente_do_mes = funcionario


            return atendente_do_mes

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_funcionario, 2: self.modificar_funcionario, 3: self.deletar_funcionario,
                        4: self.ver_funcionarios, 0: self.retornar}

        while True:
            lista_opcoes[self.__Tela_Funcionario.abre_tela()]()

    def retornar(self):
        self.__controlador_pizzaria.abre_tela_geral()

    def pegar_atendentes(self):
        atendentes = list()
        for funcionario in self.__funcionario_DAO.get_all():
            if isinstance(funcionario, Atendente):
                atendentes.append(funcionario.cpf)
        print(atendentes)
        return atendentes

    def pegar_atendente_por_cpf(self, cpf: str):
        for atendente in self.__funcionario_DAO.get_all():
            if cpf == atendente.cpf:
                return atendente.cpf
        return None

    def aumentar_pedidos_funcionario(self, cpf_funcionario):
        for cada_funcionario in self.__funcionario_DAO.get_all():
            if cada_funcionario.cpf == cpf_funcionario:
                cada_funcionario.vendas_mes += 1
