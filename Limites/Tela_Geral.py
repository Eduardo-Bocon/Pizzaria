import PySimpleGUI as sg

class Tela_Geral():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        print("componentes visuais iniciados geral")
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [
            [sg.Text('Bem vindo á nossa PIZZARIA!', font=("Helvica",25))],
            [sg.Text('Para onde desejas ir?', font=("Helvica",15))],
            [sg.Radio('Produtos',"RD1", key='1')],
            [sg.Radio('Clientes',"RD1", key='2')],
            [sg.Radio('Funcionarios',"RD1", key='3')],
            [sg.Radio('Pedidos',"RD1", key='4')],
            [sg.Radio('Pizzaria',"RD1", key='5')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1000,500)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def abre_tela_geral(self):
        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
        self.init_components()
        button, values = self.__window.Read()
        print(values)
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5

        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao    
