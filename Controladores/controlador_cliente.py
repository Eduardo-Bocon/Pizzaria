from DAOs.cliente_dao import ClienteDAO
from Limites.Tela_Cliente import Tela_Cliente
from Entidades.Pessoa.Cliente.Cliente import Cliente
from excecoes import Cliente_ja_cadastrado
from Entidades.Pessoa.Cliente.Endereco import Endereco


class ControladorCliente():

    def __init__(self, controlador_pizzaria):
        self.__cliente_DAO = ClienteDAO()
        self.__tela_Cliente = Tela_Cliente()
        self.__controlador_pizzaria = controlador_pizzaria

    def cadastrar_cliente(self):
        dados_cliente = self.__tela_Cliente.pega_dados_cliente()
        dados_endereco = self.__tela_Cliente.pega_endereco()

        cpf = str(dados_cliente["cpf"])
        cliente = self.busca_clientes(cpf)

        try:
            if cliente is None:
                cliente = Cliente(dados_cliente["nome"], cpf,
                                  dados_cliente["telefone"], dados_endereco["numero"], dados_endereco["rua"], dados_endereco["bairro"], dados_endereco["cidade"], dados_endereco["cep"])
                self.__cliente_DAO.add(cliente)
                self.__tela_Cliente.mostra_mensagem("Cadastro de cliente realizado!")

            else:
                raise Cliente_ja_cadastrado(cliente)
        except Cliente_ja_cadastrado as e:
            self.__tela_Cliente.mostra_mensagem(e)

    def deletar_cliente(self):
        self.ver_clientes()

        if not self.__cliente_DAO.get_all():
            self.__tela_Cliente.mostra_mensagem("Nenhum cliente cadastrado!")
        
        else:
            busca_cliente = self.__tela_Cliente.seleciona_cliente()
            cliente = self.busca_clientes(busca_cliente)

            if cliente is not None:
                self.__cliente_DAO.remove(cliente.cpf)
                self.__tela_Cliente.mostra_mensagem("Remoção de cadastro de cliente realizado!")


            else:
                self.__tela_Cliente.mostra_mensagem("Cliente não cadastrado!")

    def modificar_cliente(self):
        self.ver_clientes()

        if not self.__cliente_DAO.get_all():
            self.__tela_Cliente.mostra_mensagem("Nenhum cliente cadastrado!")
        
        else:
            busca_cliente = self.__tela_Cliente.seleciona_cliente()
            cliente = self.busca_clientes(busca_cliente)

            if cliente is not None:
                novos_dados_cliente = self.__tela_Cliente.pega_dados_cliente({"nome":cliente.nome, "telefone":cliente.telefone, "cpf":cliente.cpf})
                novo_endereco = self.__tela_Cliente.pega_endereco({"numero":cliente.endereco.numero, "rua":cliente.endereco.rua, "bairro":cliente.endereco.bairro, "cidade":cliente.endereco.cidade, "cep":cliente.endereco.cep})

                cliente.nome = novos_dados_cliente["nome"]
                cliente.telefone = novos_dados_cliente["telefone"]
                cliente.endereco = Endereco(numero=novo_endereco["numero"], rua=novo_endereco["rua"], bairro=novo_endereco["bairro"], cidade=novo_endereco["cidade"], cep=novo_endereco["cep"])

                self.__cliente_DAO.update(cliente)
                self.__tela_Cliente.mostra_mensagem("Modificação de cadastro de cliente realizado!")


            else:
                self.__tela_Cliente.mostra_mensagem("Cliente não cadastrado!")

    def ver_clientes(self):
        if not self.__cliente_DAO.get_all():
            self.__tela_Cliente.mostra_mensagem("Nenhum cliente cadastrado!")

        else:
            lista_clientes = []
            for cliente in self.__cliente_DAO.get_all():
                lista_clientes.append({"nome": cliente.nome, "cpf": cliente.cpf, "telefone": cliente.telefone,
                     "cidade": cliente.endereco.cidade})
            self.__tela_Cliente.mostra_clientes(lista_clientes)


    def busca_clientes(self, cpf: str):
        for cliente in self.__cliente_DAO.get_all():
            if cpf == cliente.cpf:
                return cliente
        return None

    def ver_clientes_fieis(self):
        if not self.__cliente_DAO.get_all():
            self.__tela_Cliente.mostra_mensagem("Nenhum cliente cadastrado!")

        else:
            flag = False
            for cliente in self.__cliente_DAO.get_all():
                if cliente.quantidade_pedidos >= 5:
                    self.__tela_Cliente.mostra_cliente(
                        {"nome": cliente.nome, "cpf": cliente.cpf, "telefone": cliente.telefone,
                         "cidade": cliente.endereco.cidade})
                    flag = True

            if not flag:
                self.__tela_Cliente.mostra_mensagem("Sem clientes Fiéis!")

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.modificar_cliente, 3: self.deletar_cliente,
                        4: self.ver_clientes, 5: self.ver_clientes_fieis, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_Cliente.abre_tela()]()

    def retornar(self):
        self.__controlador_pizzaria.abre_tela_geral()

    def pegar_clientes(self):
        clientes = list()
        for cliente in self.__cliente_DAO.get_all():
            if isinstance(cliente, Cliente):
                clientes.append(cliente.cpf)
        return clientes
