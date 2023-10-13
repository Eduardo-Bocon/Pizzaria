
from Limites.Tela_Cliente import Tela_Cliente
from Entidades.Pessoa.Cliente.Cliente import Cliente
from Controladores import Controlador_Pizzaria
from excecoes import Cliente_ja_cadastrado


class Controlador_Cliente():

    def __init__(self, controlador_pizzaria: Controlador_Pizzaria):
        self.__lista_Clientes = []
        self.__tela_Cliente = Tela_Cliente()
        self.__controlador_pizzaria = controlador_pizzaria

    def cadastrar_cliente(self):
        dados_cliente = self.__tela_Cliente.pega_dados_cliente()
        cpf = dados_cliente["cpf"]
        cliente = self.busca_clientes(cpf)

        try:
            if cliente == None:
                cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["telefone"], dados_cliente["endereco"])
                self.__lista_Clientes.append(cliente)
                self.__tela_Cliente.mostra_mensagem("Cadastro de cliente realizado!")

            else:
                raise Cliente_ja_cadastrado(cliente)
        except Cliente_ja_cadastrado as e:
            self.__tela_Cliente.mostra_mensagem(e)

    def deletar_cliente(self):
        self.ver_clientes()
        busca_cliente = self.__tela_Cliente.seleciona_cliente()
        cliente = self.busca_clientes(busca_cliente)

        if cliente is not None:
            self.__lista_Clientes.remove(cliente)
            self.ver_clientes()
            self.__tela_Cliente.mostra_mensagem("Remoção de cadastro de cliente realizado!")

        else:
            self.__tela_Cliente.mostra_mensagem("Cliente não cadastrado!")
    
    def modificar_cliente(self):
        self.ver_clientes()
        busca_cliente = self.__tela_Cliente.seleciona_cliente()
        cliente = self.busca_clientes(busca_cliente)

        if cliente is not None:
            novos_dados_cliente = self.__tela_Cliente.pega_dados_cliente()

            cliente.nome = novos_dados_cliente["nome"]
            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.telefone = novos_dados_cliente["telefone"]
            cliente.endereco = novos_dados_cliente["endereco"]

            self.ver_clientes()
            self.__tela_Cliente.mostra_mensagem("Modificação de cadastro de cliente realizado!")
        
        else:
            self.__tela_Cliente.mostra_mensagem("Cliente não cadastrado!")

    def ver_clientes(self):
        if self.__lista_Clientes == None:
            self.__tela_Cliente.mostra_mensagem("Nenhum cliente cadastrado!")

        else:
            for cliente in self.__lista_Clientes:
                self.__tela_Cliente.mostra_clientes({"nome": cliente.nome, "cpf": cliente.cpf, "telefone": cliente.telefone, "endereco": cliente.endereco})

    def busca_clientes(self, cpf: str):
        #busca cliente solicitado na lista de clientes
        for cliente in self.__lista_Clientes:
            if cpf == cliente.cpf:
                return cliente
        return None

    def ver_clientes_fieis(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.modificar_cliente, 3: self.deletar_cliente, 4: self.ver_clientes, 5: self.ver_clientes_fieis, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_Cliente.tela_opcoes()]()
            
    def retornar(self):
        self.__controlador_pizzaria.tela_geral()
