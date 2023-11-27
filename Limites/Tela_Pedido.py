import PySimpleGUI as sg
from excecoes import Entrada_muito_curta, Forma_de_Pagamento_Invalida, Atendente_nao_encontrado, Valor_invalido, \
    Entrada_muito_longa


class Tela_Pedido():
    
    def __init__(self, controlador):
        self.__window = None
        self.__controlador = controlador

    def init_components(self):
        print("componentes visuais iniciados pedido")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Tela Pedido', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Image("Imagens\pedido.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('O que você deseja fazer?', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [sg.Column([[sg.Button('Fazer pedido', key='1', font=font, size=size, pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Modificar pedido', key='2', font=font, size=size, pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Ver pedidos', key='3', font=font, size=size,  pad=pad)]], justification='right')],
            [sg.Column([[sg.Button('Deletar pedido', key='4', font=font, size=size,  pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Confirmar entrega pedido', key='5', font=font, size=size,  pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='right')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def abre_tela(self):

        self.init_components()
        button, values = self.__window.Read()

        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        if button == '4':
            opcao = 4
        if button == '5':
            opcao = 5

        if button == '0' or button in (None,'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def abre_tela_ver_pedidos(self):
        print("componentes visuais iniciados ver pedidos")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Tela Ver Pedidos', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Image("Imagens\pedido.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('O que você deseja fazer?', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [sg.Column([[sg.Button('Ver todos os pedidos', key='1', font=font, size=size, pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Ver os pedidos de um atendente', key='2', font=font, size=size, pad=pad)]], justification='right')],
            [sg.Column([[sg.Button('Ver os pedidos de um cliente', key='3', font=font, size=size,  pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Ver os pedidos acima de uma faixa de preço', key='4', font=font, size=size,  pad=pad)]], justification='right')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='right')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

    def pegar_dados_pedido(self, lista_atendentes: [], lista_pizzas: [], lista_bebidas: [], dados_antigos = None):


        atendente_escolhido = self.escolher_atendente(lista_atendentes)

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
                        if pizza.upper() == pizza_escolhida.upper():
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
                        if bebida.upper() == bebida_escolhida.upper():
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



        forma_de_pagamento = self.pegar_forma_pagamento()

        return { "produtos": produtos, "atendente": atendente_escolhido,
                "forma_de_pagamento": forma_de_pagamento}

    def pegar_cliente(self,dados_antigos = None):
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200, 200), (0, 0)
        size = (18, 1)

        if dados_antigos is None:
            layout = [
                [sg.Column([[sg.Text('Fazer Pedido', font=("Palatino Linotype", 30))]], justification='center',
                           pad=((0, 0), (20, 20)))],
                [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
                [sg.Column([[sg.Text('CPF do cliente:', font=font, size=size, pad=pad), sg.InputText('', key='cpf')]],
                           justification='left')],
                [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            ]
        else:
            layout = [
                [sg.Column([[sg.Text('Fazer Pedido', font=("Palatino Linotype", 30))]], justification='center',
                           pad=((0, 0), (20, 20)))],
                [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
                [sg.Column([[sg.Text('CPF do cliente:', font=font, size=size, pad=pad),
                             sg.InputText(default_text=dados_antigos['cpf'], key='cpf')]],
                           justification='left')],
                [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250, 620),
                                  icon="Imagens\pizza icone.ico").Layout(layout)

        while True:
            erro = False

            button, values = self.open()

            if dados_antigos is None:
                cpf_cliente = values['cpf']
            else:
                cpf_cliente = dados_antigos['cpf']

            try:

                # verifica se tem apenas numeros
                int(cpf_cliente)

                if len(cpf_cliente) < 8:
                    raise Entrada_muito_curta
                elif len(cpf_cliente) > 11:
                    raise Entrada_muito_longa
            except ValueError:
                erro = True
                self.mostra_mensagem("Resposta invalida! Digite apenas numeros.")
            except Entrada_muito_curta as e:
                erro = True
                self.mostra_mensagem(e)
            except Entrada_muito_longa as e:
                erro = True
                self.mostra_mensagem(e)

            if not erro:
                break
        self.close()
        return cpf_cliente



    def ver_pedido(self, dados_pedido):

        print("Código do pedido: ", dados_pedido["codigo"])
        print("Lista de produtos: ")
        for produto in dados_pedido["produtos"]:
            print(produto.nome)
        print("Cliente: ", dados_pedido["nome_cliente"])
        print("Cpf cliente: ", dados_pedido["cpf_cliente"])
        print("Atendente: ", dados_pedido["atendente"].nome)
        print("Valor: ", dados_pedido["valor"])
        print("Forma de pagamento: ", dados_pedido["forma_de_pagamento"])
        print("Data: ", dados_pedido["data"])
        print("Entregue: ", dados_pedido["entregue"])

        print("\n")

    def mostra_mensagem(self, mensagem: str):
        sg.popup("", mensagem)

    def pegar_forma_pagamento(self, formas_de_pagamento):
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200, 200), (0, 0)
        size = (18, 1)

        listbox = sg.Listbox(formas_de_pagamento, size=(20,4), enable_events=True, key='listbox', expand_y=True)

        layout = [
            [sg.Column([[sg.Text('Fazer Pedido', font=("Palatino Linotype", 30))]], justification='center',
                       pad=((0, 0), (20, 20)))],
            [sg.Column([[sg.Text('Escolha a forma de pagamento:', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [listbox],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250, 620),
                                  icon="Imagens\pizza icone.ico").Layout(layout)

        while True:
            event, values = self.__window.read()
            if event == 'listbox':
                print(values[event])
                return values[event]



    def escolher_pedido(self):
        cod = input("Digite o código do pedido: ")
        return cod

    def escolher_atendente(self):
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200, 200), (0, 0)
        size = (18, 1)

        layout = [
            [sg.Column([[sg.Text('Fazer Pedido', font=("Palatino Linotype", 30))]], justification='center',
                       pad=((0, 0), (20, 20)))],
            [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [sg.Column([[sg.Text('CPF do atentente:', font=font, size=size, pad=pad), sg.InputText('', key='cpf')]],
                       justification='left')],
            [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250, 620),
                                  icon="Imagens\pizza icone.ico").Layout(layout)

        while True:
            erro = False

            button, values = self.open()

            cpf_atendente = values['cpf']


            try:

                # verifica se tem apenas numeros
                int(cpf_atendente)

                if len(cpf_atendente) < 8:
                    raise Entrada_muito_curta
                elif len(cpf_atendente) > 11:
                    raise Entrada_muito_longa
            except ValueError:
                erro = True
                self.mostra_mensagem("Resposta invalida! Digite apenas numeros.")
            except Entrada_muito_curta as e:
                erro = True
                self.mostra_mensagem(e)
            except Entrada_muito_longa as e:
                erro = True
                self.mostra_mensagem(e)

            if not erro:
                break
        self.close()
        return cpf_atendente


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
