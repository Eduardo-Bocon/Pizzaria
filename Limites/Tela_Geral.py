import PySimpleGUI as sg

class Tela_Geral():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        print("componentes visuais iniciados")
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [[sg.Button('Produtos')], [sg.Button('Clientes')],[sg.Button('Funcionarios')],[sg.Button('Pedidos')], [sg.Button('Pizzaria')],[sg.Button('Sair')]]
        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1000,500)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def abre_tela_geral(self):
        print("---- Tela Geral ----")
        print("Opcões:")
        print("1 - Ir para tela dos produtos")
        print("2 - Ir para tela dos clientes")
        print("3 - Ir para tela dos funcionários")
        print("4 - Ir para tela de pedidos")
        print("5 - Ir para tela da pizzaria")
        print("0 - Encerrar programa")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                print("")
                if opcao < 0 or opcao > 5:
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor invalido. Insira um valor entre 0 e 5.")