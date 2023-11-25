import PySimpleGUI as sg
from excecoes import Entrada_muito_curta, Valor_invalido


class Tela_Produto:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        print("componentes visuais iniciados produto")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Tela Produtos', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Image("Imagens\produtos.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('O que você deseja fazer?', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [sg.Column([[sg.Button('Cadastrar Produto', key='1', font=font, size=size, pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Modificar Produto', key='2', font=font, size=size, pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Deletar Produto', key='3', font=font, size=size,  pad=pad)]], justification='right')],
            [sg.Column([[sg.Button('Ver Produtos', key='4', font=font, size=size,  pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='right')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def abre_tela(self):
         # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
        self.init_components()
        button, values = self.__window.Read()
        button = int(button)

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

    def pegar_dados_produto(self):
        print("componentes visuais iniciados pega dados produto")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Dados Produto', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15), sg.InputText('', key='nome')]], justification='center')],
            [sg.Column([[sg.Text('Tipo (Bebida ou Pizza?):', font=font, size=size, pad=pad), sg.InputText('', key='tipo')]], justification='left')],
            [sg.Column([[sg.Text('Nome:', font=font, size=size, pad=pad), sg.InputText('', key='nome')]], justification='center')],
            [sg.Column([[sg.Text('Preço de Compra:', font=font, size=size, pad=pad), sg.InputText('', key='preco_compra')]], justification='right')],
            [sg.Column([[sg.Text('Preço de Venda:', font=font, size=size, pad=pad), sg.InputText('', key='preco_venda')]], justification='left')],
            [sg.Column([[sg.Text('Quantidade:', font=font, size=size, pad=pad), sg.InputText('', key='quantidade')]], justification='left')],
            [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)], sg.Cancel('Retornar')], justification='center')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

        button, values = self.open()
        tipo = values['tipo']
        nome = values['nome']
        preco_compra = values['preco_compra']
        preco_venda = values['preco_venda']
        quantidade = values['quantidade']

        while True:
            try:
                if tipo.upper() != "PIZZA" and tipo.upper() != "BEBIDA":
                    raise ValueError
                break
            except ValueError:
                print("Resposta invalida! Digite \"Pizza\" ou \"Bebida\".")

        while True:
            try:
                if len(nome) < 2:
                    raise Entrada_muito_curta
                break
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                if preco_compra <= 0:
                    raise Valor_invalido("acima de 0")
                break
            except ValueError:
                print("Digite um numero.")
            except Valor_invalido as e:
                print(e)

        while True:
            try:
                if preco_venda <= 0:
                    raise Valor_invalido("maior que 0")
                elif preco_venda <= preco_compra:
                    raise Valor_invalido("maior que o valor de compra")
                break

            except ValueError:
                print("Digite um numero.")
            except Valor_invalido as e:
                print(e)

        while True:
            try:
                if quantidade <= 0:
                    raise Valor_invalido(" maior que 0")
                break
            except ValueError:
                print("Digite um numero.")
            except Valor_invalido as e:
                print(e)

        return {"tipo": tipo, "nome": nome, "preco_compra": preco_compra, "preco_venda": preco_venda, "quantidade": quantidade}

    def ver_produto(self, dados_produto):
        sg.Popup("Nome do produto: ", dados_produto["nome"])
        sg.Popup("Tipo do produto: ", dados_produto["tipo"])
        sg.Popup("Preco de compra do produto: ", dados_produto["preco_compra"])
        sg.Popup("Preco de venda do produto: ", dados_produto["preco_venda"])
        sg.Popup("Quantidade em estoque: ", dados_produto["quantidade"])
        sg.Popup("")

    def escolher_produto(self) -> str:
        print("componentes visuais iniciados seleciona produto")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        while True:
            try:
                layout = [
                    [sg.Column([[sg.Text('Selecionar Produto', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
                    [sg.Column([[sg.Text('Digite o nome do produto que deseja selecionar::', font=("Palatino Linotype", 20), pad=15), sg.InputText('', key='nome')]], justification='center')],
                    [sg.Column([[sg.Text('Nome:', font=font, size=size, pad=pad), sg.InputText('', key='nome')]], justification='left')],
                    [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)], sg.Cancel('Retornar')], justification='left')],
                ]

                self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)
                
                button, values = self.open()
                nome = values['nome']
                self.close()

                if len(nome) < 2:
                    raise Entrada_muito_curta
                break
            except Entrada_muito_curta as e:
                print(e)

        self.close()
        return nome
