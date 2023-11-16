import PySimpleGUI as sg


class Tela_Pizzaria():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        print("componentes visuais iniciados pizzaria")
        sg.ChangeLookAndFeel('DarkRed1')

        layout = [
            [sg.Text('---- Tela Pizzaria ----')],
            [sg.Button('Ver atendente do mês', key='1')],
            [sg.Button('Ver produto mais vendido', key='2')],
            [sg.Button('Ver financeiro', key='3')],
            [sg.Button('Retornar', key='0')],
            [sg.Submit("Selecionar"), sg.Cancel("Retornar")]
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1000,500)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def abre_tela(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3

        if values['0'] or button in (None,'Cancelar'):
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
