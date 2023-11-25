import PySimpleGUI as sg
from excecoes import Entrada_muito_curta, Entrada_muito_longa, Valor_abaixo_de_zero


class Tela_Cliente():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        print("componentes visuais iniciados cliente")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Tela Clientes', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Image("Imagens\cliente.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('O que você deseja fazer?', font=("Palatino Linotype", 20), pad=15)]], justification='center')],
            [sg.Column([[sg.Button('Cadastrar Cliente', key='1', font=font, size=size, pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Modificar Cliente', key='2', font=font, size=size, pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Deletar Cliente', key='3', font=font, size=size,  pad=pad)]], justification='right')],
            [sg.Column([[sg.Button('Ver Clientes', key='4', font=font, size=size,  pad=pad)]], justification='left')],
            [sg.Column([[sg.Button('Ver Clientes Fiéis', key='5', font=font, size=size,  pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='right')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def pega_dados_cliente(self):
        print("componentes visuais iniciados pega dados cliente")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Dados Cliente', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='left')],
            [sg.Column([[sg.Text('Nome:', font=font, size=size, pad=pad), sg.InputText('', key='nome')]], justification='left')],
            [sg.Column([[sg.Text('Telefone:', font=font, size=size, pad=pad), sg.InputText('', key='telefone')]], justification='left')],
            [sg.Column([[sg.Text('CPF:', font=font, size=size, pad=pad), sg.InputText('', key='cpf')]], justification='left')],
            [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='center')]
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        cpf = values['cpf']

        while True:
            try:
                if len(nome) < 3:
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

        self.close()
        return {"nome": nome, "telefone": telefone, "cpf": cpf}
    
    def pega_endereco(self):
        print("componentes visuais iniciados pega endereço")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        layout = [
            [sg.Column([[sg.Text('Dados Endereço', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
            [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='left')],
            [sg.Column([[sg.Text('Número:', font=font, size=size, pad=pad), sg.InputText('', key='numero')]], justification='left')],
            [sg.Column([[sg.Text('Rua:', font=font, size=size, pad=pad), sg.InputText('', key='rua')]], justification='left')],
            [sg.Column([[sg.Text('Bairro:', font=font, size=size, pad=pad), sg.InputText('', key='bairro')]], justification='left')],
            [sg.Column([[sg.Text('Cidade:', font=font, size=size, pad=pad), sg.InputText('', key='cidade')]], justification='left')],
            [sg.Column([[sg.Text('CEP:', font=font, size=size, pad=pad), sg.InputText('', key='cep')]], justification='left')],
            [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size,  pad=pad)]], justification='center')]
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1250,620), icon="Imagens\pizza icone.ico").Layout(layout)

        button, values = self.open()

        numero = int(values['numero'])
        rua = values['rua']
        bairro = values['bairro']
        cidade = values['cidade']
        cep = int(values['cep'])

        while True:
            try:
                if numero <= 0:
                    raise Valor_abaixo_de_zero
                break
            except ValueError:
                print("Inválido! Insira apenas números!")
            except Valor_abaixo_de_zero as e:
                print(e)

        while True:
            try:
                if len(rua) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                if len(bairro) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                if len(cidade) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                if int(cep) <= 0:
                    raise Valor_abaixo_de_zero
                
                elif len(cep) < 8:
                    raise Entrada_muito_curta
            
                elif len(cep) > 8:
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
        return {"numero": numero, "rua": rua, "bairro": bairro, "cidade": cidade, "cep": cep}
    
    def mostra_clientes(self, dados_cliente):

        string_todos_clientes = ""
        for dado in dados_cliente:
            string_todos_clientes = string_todos_clientes + "Nome do cliente: " + dado["nome"] + '\n'
            string_todos_clientes = string_todos_clientes + "CPF do cliente: ", dado["cpf"] + '\n'
            string_todos_clientes = string_todos_clientes + "Telefone do cliente: ", dado["telefone"] + '\n'
            string_todos_clientes = string_todos_clientes + "Cidade do endereço do cliente: ", dado["cidade"] + '\n\n'

        sg.Popup('Clientes Cadastrados', string_todos_clientes)

    def mostra_mensagem(self, mensagem: str):
        sg.popup("", mensagem)

    def seleciona_cliente(self):
        print("componentes visuais iniciados seleciona cliente")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200,200), (0,0)
        size = (18,1)

        while True:
            try:
                layout = [
                    [sg.Column([[sg.Text('Selecionar Cliente', font=("Palatino Linotype", 30))]], justification='center', pad=((0,0), (20,20)))],
                    [sg.Column([[sg.Text('Digite o CPF do cliente que deseja selecionar:', font=("Palatino Linotype", 20), pad=15)]], justification='left')],
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
