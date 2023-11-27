import PySimpleGUI as sg
from excecoes import Entrada_muito_curta, Valor_invalido
import PySimpleGUI as sg


class Tela_Produto:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def init_components(self, lista_pizzas):

        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200, 200), (0, 0)
        size = (18, 1)

        layout = [
            [sg.Column([[sg.Text('Tela Produtos', font=("Palatino Linotype", 30))]], justification='center',
                       pad=((0, 0), (20, 20)))],
            [sg.Column([[sg.Image("Imagens\pizza (1).png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('O que você deseja fazer?', font=("Palatino Linotype", 20), pad=15)]],
                       justification='center')],
            [sg.Column([[sg.Button('Cadastrar Produto', key='1', font=font, size=size, pad=pad)]],
                       justification='left')],
            [sg.Column([[sg.Button('Modificar Produto', key='2', font=font, size=size, pad=pad)]],
                       justification='center')],
            [sg.Column([[sg.Button('Deletar Produto', key='3', font=font, size=size, pad=pad)]],
                       justification='right')],
            [sg.Column([[sg.Button('Ver Produtos', key='4', font=font, size=size, pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size, pad=pad)]], justification='right')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250,620),
                                  icon="Imagens\pizza icone.ico").Layout(layout)

    def abre_tela(self, lista_pizzas):

        self.init_components(lista_pizzas)
        button, values = self.__window.Read()
        button = int(button)
        opcao = 0

        if button == 1:
            opcao = 1
        if button == 2:
            opcao = 2
        if button == 3:
            opcao = 3
        if button == 4:
            opcao = 4
        if button == 5:
            opcao = 5

        if button == 0 or button in (None,'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def mostra_mensagem(self, mensagem: str):
        sg.popup("", mensagem)

    def pegar_dados_produto(self, dados_antigos = None):

        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (17,1)

        if dados_antigos is None:
            layout = [
                [sg.Column([[sg.Text('Dados Produto', font=("Palatino Linotype", 30))]], justification='center',
                           pad=((0, 0), (20, 20)))],
                [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='left')],
                [sg.Column([[sg.Text('Tipo (Bebida ou Pizza?):', font=font, size=size, pad=pad),
                             sg.InputText('', key='tipo')]], justification='left')],
                [sg.Column([[sg.Text('Nome:', font=font, size=size, pad=pad), sg.InputText('', key='nome')]],
                           justification='left')],
                [sg.Column([[sg.Text('Preço de Compra:', font=font, size=size, pad=pad),
                             sg.InputText('', key='preco_compra')]], justification='left')],
                [sg.Column(
                    [[sg.Text('Preço de Venda:', font=font, size=size, pad=pad), sg.InputText('', key='preco_venda')]],
                    justification='left')],
                [sg.Column(
                    [[sg.Text('Quantidade:', font=font, size=size, pad=pad), sg.InputText('', key='quantidade')]],
                    justification='left')],
                [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            ]
        else:
            layout = [
                [sg.Column([[sg.Text('Dados Produto', font=("Palatino Linotype", 30))]], justification='center',
                           pad=((0, 0), (20, 20)))],
                [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='left')],
                [sg.Column([[sg.Text('Preço de Compra:', font=font, size=size, pad=pad),
                             sg.InputText(default_text=dados_antigos["preco_compra"], key='preco_compra')]], justification='left')],
                [sg.Column(
                    [[sg.Text('Preço de Venda:', font=font, size=size, pad=pad), sg.InputText(default_text=dados_antigos["preco_venda"], key='preco_venda')]],
                    justification='left')],
                [sg.Column(
                    [[sg.Text('Quantidade:', font=font, size=size, pad=pad), sg.InputText(default_text=dados_antigos["quantidade"], key='quantidade')]],
                    justification='left')],
                [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            ]


        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

        erro = False

        while True:
            erro = False

            button, values = self.open()

            if dados_antigos is None:
                nome = values["nome"]
                tipo = values["tipo"]
            else:
                nome = dados_antigos['nome']
                tipo = dados_antigos['tipo']

            preco_compra = values['preco_compra']
            preco_venda = values['preco_venda']
            quantidade = values['quantidade']

            try:
                if tipo.upper() != "PIZZA" and tipo.upper() != "BEBIDA":
                    raise ValueError
            except ValueError:
                erro = True
                self.mostra_mensagem("Tipo: Resposta invalida! Digite \"Pizza\" ou \"Bebida\".")

            try:
                if len(nome) < 2:
                    raise Entrada_muito_curta
            except Entrada_muito_curta as e:
                erro = True
                self.mostra_mensagem("Nome: " + str(e))

            try:
                if preco_compra == "":
                    raise ValueError
                elif float(preco_compra) <= 0:
                    raise Valor_invalido("acima de 0")

            except ValueError:
                erro = True
                self.mostra_mensagem("Preço de compra: Digite um numero.")
            except Valor_invalido as e:
                erro = True
                self.mostra_mensagem("Preço de compra: " + str(e))

            try:
                if preco_venda == "":
                    raise ValueError
                if float(preco_venda) <= 0:
                    raise Valor_invalido("maior que 0")
                elif float(preco_venda) <= float(preco_compra):
                    raise Valor_invalido("maior que o valor de compra")

            except ValueError:
                erro = True
                self.mostra_mensagem("Preço de venda: Digite um numero.")
            except Valor_invalido as e:
                erro = True
                self.mostra_mensagem("Preço de compra: " + str(e))

            try:
                if quantidade == "":
                    raise ValueError
                if int(quantidade) <= 0:
                    raise Valor_invalido(" maior que 0")
            except ValueError:
                erro = True
                self.mostra_mensagem("Quantidade: Digite um numero.")
            except Valor_invalido as e:
                erro = True
                self.mostra_mensagem("Quantidade: " + str(e))

            if not erro:
                break

        self.close()
        return {"tipo": tipo, "nome": nome, "preco_compra": float(preco_compra), "preco_venda": float(preco_venda), "quantidade": int(quantidade)}

    def ver_produto(self, dados_produto):

        string_todos_produtos = "Nome do produto: " + dados_produto["nome"] + '\n'
        string_todos_produtos = string_todos_produtos + "Tipo do produto: " + dados_produto["tipo"] + '\n'
        string_todos_produtos = string_todos_produtos + "Preço de compra: " + str(dados_produto["preco_compra"]) + '\n'
        string_todos_produtos = string_todos_produtos + "Preço de venda: " + str(dados_produto["preco_venda"]) + '\n'
        string_todos_produtos = string_todos_produtos + "Quantidade em estoque: " + str(dados_produto[
            "quantidade"]) + '\n\n'

        sg.Popup('Produtos Cadastrados', string_todos_produtos)

    def ver_produtos(self, dados_produtos):
        string_todos_produtos = ""
        for produto in dados_produtos:
            string_todos_produtos = string_todos_produtos + "Nome do produto: " + produto["nome"] + '\n'
            string_todos_produtos = string_todos_produtos + "Tipo do produto: " + produto["tipo"] + '\n'
            string_todos_produtos = string_todos_produtos + "Preço de compra: " + str(
                produto["preco_compra"]) + '\n'
            string_todos_produtos = string_todos_produtos + "Preço de venda: " + str(
                produto["preco_venda"]) + '\n'
            string_todos_produtos = string_todos_produtos + "Quantidade em estoque: " + str(produto[
                                                                                                "quantidade"]) + '\n\n'

        sg.Popup('Produtos Cadastrados', string_todos_produtos)

    def escolher_produto(self) -> str:


        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Selecionar Produto', font=("Palatino Linotype", 30))]], justification='center',
                       pad=((0, 0), (20, 20)))],
            [sg.Column(
                [[sg.Text('Digite o nome do produto que deseja selecionar::', font=("Palatino Linotype", 20), pad=15)]],
                justification='center')],
            [sg.Column([[sg.Text('Nome:', font=font, size=size, pad=pad), sg.InputText('', key='nome')]],
                       justification='left')],
            [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250, 620),
                                  icon="Imagens\pizza icone.ico").Layout(layout)

        while True:
            button, values = self.open()
            nome = values['nome']
            try:
                if len(nome) < 2:
                    raise Entrada_muito_curta
                break
            except Entrada_muito_curta as e:
                self.mostra_mensagem(e)

        self.close()
        return nome
