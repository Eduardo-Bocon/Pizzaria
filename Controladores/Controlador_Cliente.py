
from Limites.Tela_Cliente import Tela_Cliente
from Entidades.Pessoa.Cliente.Cliente import Cliente

class Controlador_CLiente():

    def __init__(self, Controlador_Pizzaria):
        self.__lista_Clientes = []
        self.__tela_Cliente = Tela_Cliente()
        self.__Controlador_Pizzaria = Controlador_Pizzaria

    def cadastrar_cliente(self, cliente: Cliente):
        #verifica repetitacao de clientes por cpf
        for verifica in self.__lista_Clientes:
            if cliente.cpf == verifica.cpf:
                return

        #recebe os dados do cliente que esta sendo cadastrado
        dados_cliente = self.__tela_Cliente.pega_dados_cliente()

        #instancia novo cliente
        novo_cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["telefone"], dados_cliente["endereco"])

        #adiciona cliente na lista_Clientes
        self.__lista_Clientes.append(novo_cliente)

    def deletar_cliente(self, cliente: Cliente):
        #seleciona um cliente pelo cpf
        busca_cliente = self.__tela_Cliente.seleciona_cliente()

        #busca o cliente atraves do cpf obtido
        cliente = self.__tela_Cliente.busca_clientes(busca_cliente)

        #remove cliente, se existir
        if cliente is not None:
            self.__lista_Clientes.remove(cliente)
        #informa um erro, se não existir
        else:
            self.__tela_Cliente.mostra_mensagem("Cliente não cadastrado!")
    
    def modificar_cliente(self, cliente: Cliente):
        #seleciona um cliente pelo cpf
        busca_cliente = self.__tela_Cliente.seleciona_cliente()

        #busca o cliente atraves do cpf obtido
        cliente = self.__tela_Cliente.busca_clientes(busca_cliente)

        if cliente is not None:
            #recebe os dados do cliente que esta sendo cadastrado
            novos_dados_cliente = self.__tela_Cliente.pega_dados_cliente()
            cliente.nome = novos_dados_cliente["nome"]
            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.telefone = novos_dados_cliente["telefone"]
            cliente.endereco = novos_dados_cliente["endereco"]
            self.__tela_Cliente.mostra_mensagem("Modificação de cadastro realizado!")
        
        else:
            self.__tela_Cliente.mostra_mensagem("Cliente não cadastrado!")

    def ver_clientes():
        pass

    def busca_clientes(self, cpf: str):
        #busca cliente solicitado na lista de clientes
        for cliente in self.__lista_Clientes:
            if cpf == cliente.cpf:
                return cliente
        return None

    def ver_clientes_fieis():
        pass

    def abre_tela():
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.modificar_cliente, 3: self.deletar_cliente, 4: self.ver_clientes, 5: self.ver_clientes_fieis, 0: self.retornar}

        while True:
            lista_opcoes[self.__Tela_Cliente.tela_opcoes()]()
            
    def retornar():
        self.__Controlador_Pizzaria.tela_geral()

