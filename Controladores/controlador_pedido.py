import datetime
from collections import Counter

from DAOs.pedido_dao import PedidoDAO
from Entidades.Pedido.Forma_de_Pagamento import Forma_de_Pagamento
from Limites.Tela_Pedido import Tela_Pedido
from Entidades.Pedido.Pedido import Pedido


class ControladorPedido():

    def __init__(self, controlador_pizzaria):
        self.__pedido_DAO = PedidoDAO()
        self.__tela = Tela_Pedido(self)
        self.__controlador_pizzaria = controlador_pizzaria
        self.__proximo_codigo = 1

    def fazer_pedido(self):

        dados_pedido = self.__tela.pegar_dados_pedido(lista_atendentes=self.__controlador_pizzaria.pegar_atendentes(),
                                                      lista_pizzas=self.__controlador_pizzaria.pegar_pizzas(),
                                                      lista_bebidas=self.__controlador_pizzaria.pegar_bebidas())

        # pegando a data atual
        data = datetime.datetime.now()

        pedido = Pedido(produtos=dados_pedido["produtos"],
                        cliente=self.__controlador_pizzaria.pegar_cliente_por_cpf(
                            dados_pedido["cpf"]),
                        atendente=dados_pedido["atendente"],
                        forma_de_pagamento=dados_pedido["forma_de_pagamento"],
                        data=data, codigo=self.__proximo_codigo)

        self.__pedido_DAO.add(pedido)
        self.__proximo_codigo += 1
        self.__controlador_pizzaria.aumentar_pedidos_funcionario(dados_pedido["atendente"])

    def deletar_pedido(self):

        self.ver_pedidos()
        codigo = self.__tela.escolher_pedido()
        pedido = self.pegar_pedido(codigo)

        if pedido is not None:
            self.__pedido_DAO.remove(pedido)
            self.ver_pedidos()
        else:
            self.__tela.mostra_mensagem("Erro: pedido não existente")

    def pegar_pedido(self, codigo):
        for pedido in self.__pedido_DAO.get_all():
            if pedido.codigo == codigo:
                return pedido
        return None

    def ver_pedidos(self):

        for pedido in self.__pedido_DAO.get_all():
            self.__tela.ver_pedido({"codigo": pedido.codigo, "produtos": pedido.produtos,
                                    "nome_cliente": pedido.cliente.nome, "cpf_cliente": pedido.cliente.cpf,
                                    "atendente": pedido.atendente, "valor": pedido.calcula_preco(),
                                    "forma_de_pagamento": pedido.forma_pagamento, "data": pedido.data,
                                    "entregue": pedido.entregue})

    def ver_pedidos_com_filtro(self):
        lista_opcoes = {1: self.ver_pedidos, 2: self.ver_pedidos_atendente, 3: self.ver_pedidos_cliente,
                        4: self.ver_pedidos_por_valor,
                        0: self.retornar}
        while 1:
            lista_opcoes[self.__tela.abre_tela_ver_pedidos()]()

    def ver_pedidos_atendente(self):
        atendente = self.__tela.escolher_atendente(self.__controlador_pizzaria.pegar_atendentes())
        existe = False
        for pedido in self.__pedido_DAO.get_all():
            if pedido.atendente == atendente:
                existe = True
                self.__tela.ver_pedido({"codigo": pedido.codigo, "produtos": pedido.produtos,
                                        "nome_cliente": pedido.cliente.nome, "cpf_cliente": pedido.cliente.cpf,
                                        "atendente": pedido.atendente, "valor": pedido.calcula_preco(),
                                        "forma_de_pagamento": pedido.forma_pagamento, "data": pedido.data,
                                        "entregue": pedido.entregue})
        if not existe:
            self.__tela.mostra_mensagem("Não tem pedidos com esse atendente.")

    def ver_pedidos_cliente(self):
        cliente = self.__tela.escolher_cliente(self.__controlador_pizzaria.pegar_clientes())
        existe = False
        for pedido in self.__pedido_DAO.get_all():
            if pedido.cliente == cliente:
                existe = True
                self.__tela.ver_pedido({"codigo": pedido.codigo, "produtos": pedido.produtos,
                                        "nome_cliente": pedido.cliente.nome, "cpf_cliente": pedido.cliente.cpf,
                                        "atendente": pedido.atendente, "valor": pedido.calcula_preco(),
                                        "forma_de_pagamento": pedido.forma_pagamento, "data": pedido.data,
                                        "entregue": pedido.entregue})
        if not existe:
            self.__tela.mostra_mensagem("Não tem pedidos com esse cliente.")

    def ver_pedidos_por_valor(self):
        valor = self.__tela.escolher_valor()
        existe = False
        for pedido in self.__pedido_DAO.get_all():
            if pedido.calcula_preco() >= valor:
                existe = True
                self.__tela.ver_pedido({"codigo": pedido.codigo, "produtos": pedido.produtos,
                                        "nome_cliente": pedido.cliente.nome, "cpf_cliente": pedido.cliente.cpf,
                                        "atendente": pedido.atendente, "valor": pedido.calcula_preco(),
                                        "forma_de_pagamento": pedido.forma_pagamento, "data": pedido.data,
                                        "entregue": pedido.entregue})
        if not existe:
            self.__tela.mostra_mensagem("Não tem pedidos acima desse valor.")

    def modificar_pedido(self):
        self.ver_pedidos()
        codigo = self.__tela.escolher_pedido()
        pedido = self.pegar_pedido(codigo)

        if pedido is not None:
            novos_dados_pedido = self.__tela.pegar_dados_pedido(lista_atendentes=
                                                                self.__controlador_pizzaria.pegar_atendentes,
                                                                lista_pizzas=
                                                                self.__controlador_pizzaria.pegar_pizzas,
                                                                lista_bebidas=
                                                                self.__controlador_pizzaria.pegar_bebidas)

            pedido.cliente = novos_dados_pedido["cliente"]
            pedido.produtos = novos_dados_pedido["produtos"]
            pedido.atendente = novos_dados_pedido["atendente"]
            pedido.forma_de_pagamento = novos_dados_pedido["forma_de_pagamento"]
            pedido.cliente = novos_dados_pedido["cliente"]

            self.ver_pedidos()
        else:
            self.__tela.mostra_mensagem("Erro: pedido não existente")

    def abre_tela(self):
        lista_opcoes = {1: self.fazer_pedido, 2: self.modificar_pedido, 3: self.ver_pedidos_com_filtro,
                        4: self.deletar_pedido, 5: self.pedido_entregue,
                        0: self.retornar}

        while 1:
            lista_opcoes[self.__tela.abre_tela()]()

    def retornar(self):
        self.__controlador_pizzaria.abre_tela_geral()

    def pedido_entregue(self):

        self.ver_pedidos()

        codigo = self.__tela.escolher_pedido()

        existe = False

        for pedido in self.__pedido_DAO.get_all():
            print("Verificando pedido: {}".format(pedido.codigo))

            if pedido.codigo == int(codigo):
                pedido.entregue = True
                existe = True
            else:
                print("{} não é igual a {}".format(pedido.codigo, codigo))

        if not existe:
            self.__tela.mostra_mensagem("Erro: pedido não existente")

    def pegar_receitas(self):

        receitas = 0

        for pedido in self.__pedido_DAO.get_all():
            receitas += pedido.calcula_preco()

        return receitas

    def pegar_despesas(self):

        despesas = 0

        for pedido in self.__pedido_DAO.get_all():
            despesas += pedido.calcula_gastos()

        return despesas

    def pegar_produto_mais_vendido(self):

        quantidade = 0
        produto_mais_vendido = None

        todos_os_produtos = list()

        if not self.__pedido_DAO.get_all():
            return {"produto": "Sem produtos cadastrados", "quantidade": "-"}

        for pedido in self.__pedido_DAO.get_all():
            for produto in pedido.produtos:
                todos_os_produtos.append(produto)

        # faz a contagem de aparicoes
        contador = Counter(todos_os_produtos)

        # pega o mais vendido
        produto_mais_vendido = contador.most_common(1)[0][0]

        # pega a quantidade de vezes que apareceu
        quantidade = contador.most_common(1)[0][1]

        return {"produto": produto_mais_vendido, "quantidade": quantidade}

    def pegar_formas_pagamento(self):
        return Forma_de_Pagamento
