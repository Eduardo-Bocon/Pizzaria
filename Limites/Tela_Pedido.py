from Entidades.Pedido.Forma_de_Pagamento import Forma_de_Pagamento
from excecoes import Entrada_muito_curta, Forma_de_Pagamento_Invalida, Atendente_nao_encontrado, Valor_invalido


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
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor invalido. Insira um valor entre 0 e 4.")

    def pegar_dados_pedido(self, lista_atendentes, lista_pizzas, lista_bebidas):

        print("Insira os dados do novo pedido:")

        while True:
            try:
                cpf_cliente = input("Informe o cpf do cliente: ")
                if len(cpf_cliente) < 11:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Resposta invalida! Digite um cpf no formato XXXXXXXXXXX.")

        produtos = list()

        print("Vamos ver os produtos do pedido.")

        while True:
            print("1 - adicionar pizza")
            print("2 - adicionar bebida")
            print("3 - continuar o pedido")

            while True:
                try:
                    escolha = int(input("O que deseja fazer?"))
                    if escolha < 1 or escolha > 3:
                        raise Valor_invalido(" 1,2,3")
                    break
                except ValueError:
                    print("Insira um numero.")

            if escolha == 1:
                while True:

                    pizza_escolhida = input("Insira o nome da pizza: ")

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

                bebida_escolhida = input("Insira o nome da bebida: ")

                existe = False

                for bebida in lista_bebidas:
                    if bebida.sabor.upper() == bebida_escolhida.upper():
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


        while True:

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
            else:
                if atendente_escolhido != None:
                    break

        forma_de_pagamento = self.pegar_forma_pagamento()


        return {"cpf": cpf_cliente, "produto": produtos, "atendente": atendente_escolhido, "forma_de_pagamento": forma_de_pagamento}

    def ver_pedido(self, dados_pedido):

        print("Código do pedido: ", dados_pedido["codigo"])
        print("Lista de produtos: ", dados_pedido["produtos"])
        print("Cliente: ", dados_pedido["nome_cliente"])
        print("Cpf cliente: ", dados_pedido["cpf_cliente"])
        print("Atendente: ", dados_pedido["atendente"])
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

            forma_escolhida = input("Insira a forma de pagamento: ")

            existe = False
            for forma in Forma_de_Pagamento:
                if forma_escolhida.upper() == forma.value.upper():
                    existe = True
                    break

            if not existe:
                raise Forma_de_Pagamento_Invalida
            else:
                break

        return forma_escolhida

    def escolher_pedido(self):
        cod = input("Digite o código do pedido: ")
        return cod






