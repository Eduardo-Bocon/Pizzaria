from Entidades.Pedido.Forma_de_Pagamento import Forma_de_Pagamento
from Entidades.Produtos.Bebida import Bebida
from Entidades.Produtos.Pizza import Pizza
from excecoes import Entrada_muito_curta, Forma_de_Pagamento_Invalida, Atendente_nao_encontrado, Valor_invalido, \
    Entrada_muito_longa


class Tela_Pedido():

    def abre_tela(self):
        print("---- Tela Pedidos ----")
        print("Opcões:")
        print("1 - Fazer pedido")
        print("2 - Modificar pedido")
        print("3 - Ver pedidos")
        print("4 - Deletar pedido")
        print("5 - Confirmar entrega pedido")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                if opcao < 0 or opcao > 5:
                    raise Valor_invalido("0 até 5")
                return opcao
            except ValueError:
                print("Digite um numero.")
            except Valor_invalido as e:
                print(e)

    def abre_tela_ver_pedidos(self):
        print("Opcões:")
        print("1 - Ver todos os pedidos")
        print("2 - Ver os pedidos de um atendente")
        print("3 - Ver os pedidos de um cliente")
        print("4 - Ver os pedidos acima de uma faixa de preço")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                print("")
                if opcao < 0 or opcao > 4:
                    raise Valor_invalido("0 até 4")
                return opcao
            except ValueError:
                print("Digite um numero.")
            except Valor_invalido as e:
                print(e)

    def pegar_dados_pedido(self, lista_atendentes: [], lista_pizzas: [], lista_bebidas: []):

        print("Insira os dados do novo pedido.")

        while True:
            try:
                cpf_cliente = input("Informe o cpf do cliente: ")

                # verifica se tem apenas numeros
                int(cpf_cliente)

                if len(cpf_cliente) < 9:
                    raise Entrada_muito_curta
                elif len(cpf_cliente) > 11:
                    raise Entrada_muito_longa
                break
            except ValueError:
                print("Resposta invalida! Digite apenas numeros.")
            except Entrada_muito_curta as e:
                print(e)
            except Entrada_muito_longa as e:
                print(e)

        produtos = list()

        print("Agora vamos escolher os produtos do pedido.")

        while True:
            print("1 - adicionar pizza")
            print("2 - adicionar bebida")
            print("3 - continuar o pedido")

            while True:
                try:
                    escolha = int(input("O que deseja fazer?"))
                    if escolha < 1 or escolha > 3:
                        raise Valor_invalido("1,2,3")
                    break
                except ValueError:
                    print("Insira um numero.")
                except Valor_invalido as e:
                    print(e)

            if escolha == 1:
                while True:
                    while True:
                        try:
                            pizza_escolhida = input("Insira o nome da pizza: ")
                            if pizza_escolhida == "0":
                                break
                            if len(pizza_escolhida) < 2:
                                raise Entrada_muito_curta
                            break
                        except Entrada_muito_curta as e:
                            print(e)
                    if pizza_escolhida == "0":
                        break
                    existe = False

                    for pizza in lista_pizzas:
                        if pizza.sabor.upper() == pizza_escolhida.upper():
                            existe = True
                            if pizza.quantidade > 0:
                                produtos.append(pizza)
                                pizza.diminuir_estoque(1)
                            else:
                                print("Não temos essa pizza no estoque.")
                    if not existe:
                        print("Pizza não existe.")
                    else:
                        break
            elif escolha == 2:
                while True:
                    while True:
                        try:
                            bebida_escolhida = input("Insira o nome da bebida: ")
                            if bebida_escolhida == "0":
                                break
                            if len(bebida_escolhida) < 2:
                                raise Entrada_muito_curta
                            break
                        except Entrada_muito_curta as e:
                            print(e)
                    if bebida_escolhida == "0":
                        break
                    existe = False

                    for bebida in lista_bebidas:
                        if bebida.tipo.upper() == bebida_escolhida.upper():
                            existe = True
                            if bebida.quantidade > 0:
                                produtos.append(bebida)
                                bebida.diminuir_estoque(1)
                            else:
                                print("Não temos essa bebida no estoque.")
                    if not existe:
                        print("Bebida não existe.")
                    else:
                        break

            elif escolha == 3:
                break

        atendente_escolhido = self.escolher_atendente(lista_atendentes)

        forma_de_pagamento = self.pegar_forma_pagamento()

        return {"cpf": cpf_cliente, "produtos": produtos, "atendente": atendente_escolhido, "forma_de_pagamento": forma_de_pagamento}

    def ver_pedido(self, dados_pedido):

        print("Código do pedido: ", dados_pedido["codigo"])
        print("Lista de produtos: ")
        for produto in dados_pedido["produtos"]:
            if isinstance(produto, Pizza):
                print(produto.sabor)
            elif isinstance(produto, Bebida):
                print(produto.tipo)
        print("Cliente: ", dados_pedido["nome_cliente"])
        print("Cpf cliente: ", dados_pedido["cpf_cliente"])
        print("Atendente: ", dados_pedido["atendente"].nome)
        print("Valor: ", dados_pedido["valor"])
        print("Forma de pagamento: ", dados_pedido["forma_de_pagamento"])
        print("Data: ", dados_pedido["data"])
        print("Entregue: ", dados_pedido["entregue"])

        print("\n")

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def pegar_forma_pagamento(self):

        for forma in Forma_de_Pagamento:
            print(forma.value)

        while 1:
            try:
                forma_escolhida = input("Insira a forma de pagamento: ")

                existe = False
                for forma in Forma_de_Pagamento:
                    if forma_escolhida.upper() == forma.value.upper():
                        existe = True
                        break

                if not existe:
                    raise Forma_de_Pagamento_Invalida
                break
            except Forma_de_Pagamento_Invalida as e:
                print(e)

        return forma_escolhida

    def escolher_pedido(self):
        cod = input("Digite o código do pedido: ")
        return cod

    def escolher_atendente(self, lista_atendentes:[]):

        while True:

            try:
                nome_atendente = input("Insira o nome do atendente: ")

                atendente_escolhido = None

                existe = False

                for atendente in lista_atendentes:
                    if nome_atendente.upper() == atendente.nome.upper():
                        existe = True
                        atendente_escolhido = atendente

                if len(nome_atendente) < 2:
                    raise Entrada_muito_curta
                elif not existe:
                    raise Atendente_nao_encontrado
                return atendente_escolhido

            except Entrada_muito_curta as e:
                print(e)
            except Atendente_nao_encontrado as e:
                print(e)

    def escolher_cliente(self, lista_clientes):

        while True:
            try:
                nome_cliente = input("Insira o nome do cliente: ")

                cliente_escolhido = None

                existe = False

                if lista_clientes is not None:
                    for cliente in lista_clientes:
                        if nome_cliente.upper() == cliente.nome.upper():
                            existe = True
                            cliente_escolhido = cliente

                if len(nome_cliente) < 2:
                    raise Entrada_muito_curta
                elif not existe:
                    raise Atendente_nao_encontrado

                return cliente_escolhido
            except Entrada_muito_curta as e:
                print(e)
            except Atendente_nao_encontrado as e:
                print(e)

    def escolher_valor(self):
        try:
            valor = float(input("Digite o valor: "))
            if valor < 0:
                raise Valor_invalido("acima de 0")
            return valor
        except ValueError:
            print("Erro! Digite um valor.")
        except Valor_invalido as e:
            print(e)



