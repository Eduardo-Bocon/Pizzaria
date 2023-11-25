import PySimpleGUI as sg
from excecoes import Entrada_muito_curta, Entrada_muito_longa, Valor_abaixo_de_zero


class Tela_Funcionario():

    def __init__(self):
        self.__window = None


    def init_components(self):
        print("componentes visuais iniciados funcionario")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Tela Funcionários', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Image("Imagens\carteira-de-identidade.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('O que você deseja fazer?', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [sg.Column([[sg.Button('Cadastrar Funcionário', key='1', font=font, size=size, pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Modificar Funcionário', key='2', font=font, size=size, pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Deletar Funcionário', key='3', font=font, size=size,  pad=pad)]], justification='right')],
            [sg.Column([[sg.Button('Ver Funcionarios', key='4', font=font, size=size,  pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='right')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def pega_dados_funcionario(self):
        print("componentes visuais iniciados pega dados funcionario")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Dados Funcionário', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='left')],
            [sg.Column([[sg.Text('Nome:', font=font, size=size, pad=pad), sg.InputText('', key='nome')]], justification='left')],
            [sg.Column([[sg.Text('Telefone:', font=font, size=size, pad=pad), sg.InputText('', key='telefone')]], justification='left')],
            [sg.Column([[sg.Text('CPF:', font=font, size=size, pad=pad), sg.InputText('', key='cpf')]], justification='left')],
            [sg.Column([[sg.Text('Salário:', font=font, size=size, pad=pad), sg.InputText('', key='salario')]], justification='left')],
            [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='center')]

        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        cpf = values['cpf']
        salario = values['salario']

        while True:
            try:
                if len(nome) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                if int(telefone) <= 0:
                    raise Valor_abaixo_de_zero
                
                elif len(telefone) < 6:
                    raise Entrada_muito_curta
                
                elif len(telefone) > 12:
                    raise Entrada_muito_longa

                break
            except ValueError:
                print("Entrada inválida!")
            except Valor_abaixo_de_zero as e:
                print(e)
            except Entrada_muito_curta as e:
                print(e)
            except Entrada_muito_longa as e:
                print(e)

        while True:
            try:
                if int(cpf) <= 0:
                    raise Valor_abaixo_de_zero
                
                elif len(cpf) < 9:
                    raise Entrada_muito_curta
            
                elif len(cpf) > 11:
                    raise Entrada_muito_longa
                break
            except ValueError:
                print("Entrada inválida!")
            except Valor_abaixo_de_zero as e:
                print(e)
            except Entrada_muito_curta as e:
                print(e)
            except Entrada_muito_longa as e:
                print(e)

        while True:
            try:
                if int(salario) <= 0:
                    raise Valor_abaixo_de_zero
                break
            except ValueError:
                print("Entrada inválida!")

        return {"nome": nome, "telefone": telefone, "cpf": cpf, "salario": salario}

    def mostra_funcionarios(self, dados_funcionario):
        sg.Popup("Nome do funcionário: ", dados_funcionario["nome"])
        sg.Popup("CPF do funcionário: ", dados_funcionario["cpf"])
        sg.Popup("Telefone do funcionário: ", dados_funcionario["telefone"])
        sg.Popup("Salário do funcionário: ", dados_funcionario["salario"])
        sg.Popup("")

    def mostra_mensagem(self, mensagem: str):
        sg.popup("", mensagem)

    def seleciona_funcionario(self):
        print("componentes visuais iniciados seleciona funcionario")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        while True:
            try:
                layout = [
                    [sg.Column([[sg.Text('Selecionar Funcionário', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
                    [sg.Column([[sg.Text('Digite o CPF do funcionário que deseja selecionar:', font=("Palatino Linotype", 20), pad=15), sg.InputText('', key='nome')]], justification='left')],
                    [sg.Column([[sg.Text('CPF:', font=font, size=size, pad=pad), sg.InputText('', key='cpf')]], justification='left')],
                    [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
                    [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='center')]
                ]

                self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)
                
                button, values = self.open()
                cpf = values['cpf']
                self.close()

                if int(cpf) <= 0:
                    raise Valor_abaixo_de_zero
                
                elif len(cpf) < 9:
                    raise Entrada_muito_curta
            
                elif len(cpf) > 11:
                    raise Entrada_muito_longa
                break
            except ValueError:
                print("Entrada inválida!")
            except Valor_abaixo_de_zero as e:
                print(e)
            except Entrada_muito_curta as e:
                print(e)
            except Entrada_muito_longa as e:
                print(e)

        self.close()
        return cpf
    
    def escolhe_funcao(self):
        print("componentes visuais iniciados escolhe funcao")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        while True:
            layout = [
                [sg.Column([[sg.Button('Atendente', key='1', font=font, size=size, pad=pad)]], justification='left')],
                [sg.Column([[sg.Button('Gerente', key='2', font=font, size=size, pad=pad)]], justification='right')],
                [sg.Column([[sg.Button('Pizzaiolo', key='3', font=font, size=size,  pad=pad)]], justification='left')],
                [sg.Column([[sg.Button('Entregador', key='4', font=font, size=size,  pad=pad)]], justification='right')],
            ]

            self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)
            
            button, values = self.open()
            funcao = button
            self.close()
            return funcao


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

        if button == 0 or button in (None,'Cancelar'):
            opcao = 0

        self.close()
        return opcao
