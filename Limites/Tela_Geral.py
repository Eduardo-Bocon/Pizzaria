import PySimpleGUI as sg

class Tela_Geral():

    def __init__(self):
        self.__window = None


    def init_components(self):
        print("componentes visuais iniciados geral")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Bem vindo á nossa PIZZARIA!', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Image("Imagens\pizza.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('Para onde você quer ir?', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [sg.Column([[sg.Button('Produtos', key='1', font=font, size=size, pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Clientes', key='2', font=font, size=size)]], justification='center')],
            [sg.Column([[sg.Button('Funcionarios', key='3', font=font, size=size,  pad=pad)]], justification='right')],
            [sg.Column([[sg.Button('Pedidos', key='4', font=font, size=size,  pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Pizzaria', key='5', font=font, size=size)]], justification='center')],
            [sg.Column([[sg.Button('Finalizar sistema', key='0', font=font, size=size,  pad=pad)]], justification='right')]
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def abre_tela_geral(self):
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
