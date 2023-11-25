import PySimpleGUI as sg


class Tela_Pizzaria():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        print("componentes visuais iniciados pizzaria")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Tela Pizzaria', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Image("Imagens\estatisticas.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('O que você deseja fazer?', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [sg.Column([[sg.Button('Ver atendente do mês', key='1', font=font, size=size, pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Ver produto mais vendido', key='2', font=font, size=size)]], justification='center')],
            [sg.Column([[sg.Button('Ver financeiro', key='3', font=font, size=size,  pad=pad)]], justification='right')],
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
        opcao = 0

        if button == 1:
            opcao = 1
        if button == 2:
            opcao = 2
        if button == 3:
            opcao = 3
        if button == 0 or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def mostra_mensagem(self, mensagem: str):
        sg.popup("", mensagem)

    def atendente_do_mes(self, atendente_do_mes):
        if atendente_do_mes is None:
            sg.Popup("Não há pedidos com atendentes.")
        else:
            sg.Popup("Atendente do mês: ",atendente_do_mes.nome)

    def produto_mais_vendido(self, produto_mais_vendido):
        if produto_mais_vendido is None:
            sg.Popup("Não há pedidos com produtos.")
        else:
            sg.Popup("Produto mais vendido do mês: ", produto_mais_vendido["produto"].nome)
            sg.Popup("Quantidade: ", produto_mais_vendido["quantidade"])

    def mostrar_financeiro(self, salarios, despesas, receitas):
        sg.Popup("Total de salários: ", (salarios))
        sg.Popup("Total de despesas: ", (despesas))
        sg.Popup("Total de receitas: ", (receitas))
        sg.Popup("Lucro total: ", (receitas - despesas))
        sg.Popup("")
