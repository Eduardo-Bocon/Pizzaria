import PySimpleGUI as sg

class Tela_Geral():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self, ):
        print("componentes visuais iniciados geral")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 30)
        layout = [
            [sg.Column([[sg.Text('Bem vindo á nossa PIZZARIA!', font=("Palatino Linotype", 60))]], justification='center', pad=((0,0), (60,40)))],
            [sg.Column([[sg.Image("Imagens\pizza.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('Para onde você quer ir?', font=("Palatino Linotype", 50), pad=30)]], justification='center')],
            [sg.Column([[sg.Button('Produtos', key='1', font=("Palatino Linotype", 20), size=(15,1), pad=((300,300), (0,0)))]], justification='left')],
            [sg.Column([[sg.Button('Clientes', key='2', font=("Palatino Linotype", 20), size=(15,1))]], justification='center')],
            [sg.Column([[sg.Button('Funcionarios', key='3', font=("Palatino Linotype", 20), size=(15,1),  pad=((300,300), (0,0)))]], justification='right')],
            [sg.Column([[sg.Button('Pedidos', key='4', font=("Palatino Linotype", 20), size=(15,1),  pad=((300,300), (0,0)))]], justification='left')],
            [sg.Column([[sg.Button('Pizzaria', key='5', font=("Palatino Linotype", 20), size=(15,1))]], justification='center')],
            [sg.Column([[sg.Button('Finalizar sistema', key='0', font=("Palatino Linotype", 20), size=(15,1),  pad=((300,300), (0,0)))]], justification='right')]
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1920,1080), icon="Imagens\pizza icone.ico").Layout(layout)

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

        print(opcao)
        self.close()
        return opcao    
