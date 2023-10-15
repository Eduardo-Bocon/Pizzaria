import datetime

from Limites.Tela_Pedido import Tela_Pedido
from Entidades.Pedido.Pedido import Pedido



class Controlador_Pedido():

    def __init__(self, controlador_pizzaria):
        self.__lista_pedidos = []
        self.__tela = Tela_Pedido()
        self.__controlador_pizzaria = controlador_pizzaria
        self.__proximo_codigo = 1

    def fazer_pedido(self):
        dados_pedido = self.__tela.pegar_dados_pedido(lista_atendentes=self.__controlador_pizzaria.pegar_atendentes,
                                                      lista_pizzas=self.__controlador_pizzaria.pegar_pizzas,
                                                      lista_bebidas=self.__controlador_pizzaria.pegar_bebidas)

        # pegando a data atual
        data = datetime.datetime.now()

        self.__lista_pedidos.append(Pedido(produtos=dados_pedido["produtos"],
                                           cliente=self.__controlador_pizzaria.pegar_cliente_por_cpf(
                                               dados_pedido["cpf"]),
                                           atendente=dados_pedido["atendente"],
                                           forma_de_pagamento=dados_pedido["forma_de_pagamento"],
                                           data=data, codigo=self.__proximo_codigo))
        self.__proximo_codigo += 1

    def deletar_pedido(self):

        self.ver_pedidos()
        codigo = self.__tela.escolher_pedido()
        pedido = self.pegar_pedido(codigo)

        if pedido is not None:
            self.__lista_pedidos.remove(pedido)
            self.ver_pedidos()
        else:
            self.__tela.mostra_mensagem("Erro: pedido não existente")

    def pegar_pedido(self, codigo):
        for pedido in self.__lista_pedidos:
            if pedido.codigo == codigo:
                return pedido
        return None

    def ver_pedidos(self, cliente=None):
        if cliente == None:
            for pedido in self.__lista_pedidos:
                self.__tela.ver_pedido({"codigo": pedido.codigo, "produtos": pedido.produtos,
                                        "nome_cliente": pedido.cliente.nome, "cpf_cliente": pedido.cliente.cpf,
                                        "atendente": pedido.atendente, "valor": pedido.calcula_preco(),
                                        "forma_de_pagamento": pedido.forma_pagamento, "data": pedido.data,
                                        "entregue": pedido.entregue})
        else:
            for pedido in self.__lista_pedidos:
                if pedido.cliente.cpf == cliente.cpf:
                    self.__tela.ver_pedido({"codigo": pedido.codigo, "produtos": pedido.produtos,
                                            "nome_cliente": pedido.cliente.nome, "cpf_cliente": pedido.cliente.cpf,
                                            "atendente": pedido.atendente, "valor": pedido.calcula_preco(),
                                            "forma_de_pagamento": pedido.forma_pagamento, "data": pedido.data,
                                            "entregue": pedido.entregue})

    def modificar_pedido(self):
        self.ver_pedidos()
        codigo = self.__tela.escolher_pedido()
        pedido = self.pegar_pedido(codigo)

        if (pedido is not None):
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
        lista_opcoes = {1: self.fazer_pedido, 2: self.modificar_pedido, 3: self.deletar_pedido,
                        4: self.ver_pedidos, 5: self.pedido_entregue,
                        0: self.retornar}

        while 1:
            lista_opcoes[self.__tela.abre_tela()]()

    def retornar(self):
        self.__controlador_pizzaria.abre_tela_geral()

    def pedido_entregue(self):

        self.ver_pedidos()

        codigo = self.__tela.escolher_pedido()

        existe = False

        for pedido in self.__lista_pedidos:
            if pedido.codigo == codigo:
                pedido.entregue = True
                existe = True

        if not existe:
            self.__tela.mostra_mensagem("Erro: pedido não existente")
