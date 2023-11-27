import PySimpleGUI as sg
from excecoes import Entrada_muito_curta, Entrada_muito_longa, Valor_abaixo_de_zero


class Tela_Funcionario():

    def __init__(self):
        self.__window = None

    def init_components(self):

        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200, 200), (0, 0)
        size = (18, 1)

        layout = [
            [sg.Column([[sg.Text('Tela Funcionários', font=("Palatino Linotype", 30))]], justification='center',
                       pad=((0, 0), (20, 20)))],
            [sg.Column([[sg.Image("Imagens\carteira-de-identidade.png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('O que você deseja fazer?', font=("Palatino Linotype", 20), pad=15)]],
                       justification='center')],
            [sg.Column([[sg.Button('Cadastrar Funcionário', key='1', font=font, size=size, pad=pad)]],
                       justification='left')],
            [sg.Column([[sg.Button('Modificar Funcionário', key='2', font=font, size=size, pad=pad)]],
                       justification='center')],
            [sg.Column([[sg.Button('Deletar Funcionário', key='3', font=font, size=size, pad=pad)]],
                       justification='right')],
            [sg.Column([[sg.Button('Ver Funcionarios', key='4', font=font, size=size, pad=pad)]],
                       justification='left')],
            [sg.Column([[sg.Button('Retornar', key='0', font=font, size=size, pad=pad)]], justification='right')],
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250, 620),
                                  icon="Imagens\pizza icone.ico").Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def pega_dados_funcionario(self, dados_antigos=None):

        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200, 200), (0, 0)
        size = (18, 1)

        if dados_antigos is None:
            layout = [
                [sg.Column([[sg.Text('Dados Funcionário', font=("Palatino Linotype", 30))]], justification='center',
                           pad=((0, 0), (20, 20)))],
                [sg.Column([[sg.Text('Insira:', font=("Palatino Linotype", 20), pad=15)]], justification='left')],
                [sg.Column([[sg.Text('Nome:', font=font, size=size, pad=pad), sg.InputText('', key='nome')]],
                           justification='left')],
                [sg.Column([[sg.Text('Telefone:', font=font, size=size, pad=pad), sg.InputText('', key='telefone')]],
                           justification='left')],
                [sg.Column([[sg.Text('CPF:', font=font, size=size, pad=pad), sg.InputText('', key='cpf')]],
                           justification='left')],
                [sg.Column([[sg.Text('Salário:', font=font, size=size, pad=pad), sg.InputText('', key='salario')]],
                           justification='left')],
                [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            ]
        else:
            layout = [
                [sg.Column([[sg.Text('Dados Funcionário', font=("Palatino Linotype", 30))]], justification='center',
                           pad=((0, 0), (20, 20)))],
                [sg.Column([[sg.Text('Insira', font=("Palatino Linotype", 20), pad=15)]], justification='left')],
                [sg.Column([[sg.Text('Nome:', font=font, size=size, pad=pad),
                             sg.InputText(default_text=dados_antigos["nome"], key='nome')]],
                           justification='left')],
                [sg.Column([[sg.Text('Telefone:', font=font, size=size, pad=pad),
                             sg.InputText(default_text=dados_antigos["telefone"], key='telefone')]],
                           justification='left')],
                [sg.Column([[sg.Text('Salário:', font=font, size=size, pad=pad),
                             sg.InputText(default_text=dados_antigos["salario"], key='salario')]],
                           justification='left')],
                [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
            ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250, 620),
                                  icon="Imagens\pizza icone.ico").Layout(layout)

        while True:
            button, values = self.open()
            nome = values['nome']
            telefone = values['telefone']
            salario = values['salario']

            if dados_antigos is None:
                cpf = values['cpf']
            else:
                cpf = dados_antigos["cpf"]

            try:
                if len(nome) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                self.mostra_mensagem("Nome: Entrada inválida!")
            except Entrada_muito_curta as e:
                self.mostra_mensagem("Nome: " + str(e))

            try:
                if int(telefone) <= 0:
                    raise Valor_abaixo_de_zero

                elif len(telefone) < 6:
                    raise Entrada_muito_curta

                elif len(telefone) > 12:
                    raise Entrada_muito_longa

                break
            except ValueError:
                self.mostra_mensagem("Telefone: Entrada inválida!")
            except Valor_abaixo_de_zero as e:
                self.mostra_mensagem("Telefone: " + str(e))
            except Entrada_muito_curta as e:
                self.mostra_mensagem("Telefone: " + str(e))
            except Entrada_muito_longa as e:
                self.mostra_mensagem("Telefone: " + str(e))

            try:
                if int(cpf) <= 0:
                    raise Valor_abaixo_de_zero

                elif len(cpf) < 9:
                    raise Entrada_muito_curta

                elif len(cpf) > 11:
                    raise Entrada_muito_longa
                break
            except ValueError:
                self.mostra_mensagem("CPF: Entrada inválida!")
            except Valor_abaixo_de_zero as e:
                self.mostra_mensagem("CPF: " + str(e))
            except Entrada_muito_curta as e:
                self.mostra_mensagem("CPF: " + str(e))
            except Entrada_muito_longa as e:
                self.mostra_mensagem("CPF: " + str(e))

            try:
                if int(salario) <= 0:
                    raise Valor_abaixo_de_zero
                break
            except ValueError:
                self.mostra_mensagem("Salario: Entrada inválida!")
            except Valor_abaixo_de_zero as e:
                self.mostra_mensagem("Salario: " + str(e))
                
        self.close()
        return {"nome": nome, "telefone": telefone, "cpf": cpf, "salario": salario}

    def mostra_funcionario(self, dados_funcionario):
        string_todos_funcionarios = "Nome do funcionario: " + dados_funcionario["nome"] + '\n'
        string_todos_funcionarios = string_todos_funcionarios + "CPF do funcionario: " + str(dados_funcionario["cpf"]) + '\n'
        string_todos_funcionarios = string_todos_funcionarios + "Telefone do funcionario: " + dados_funcionario["telefone"] + '\n'
        string_todos_funcionarios = string_todos_funcionarios + "Salario: " + dados_funcionario[
            "salario"] + '\n\n'

        sg.Popup('Funcionarios Cadastrados', string_todos_funcionarios)

    def mostra_funcionarios(self, dados_funcionarios):
        string_todos_funcionarios = ""
        for funcionario in dados_funcionarios:
            string_todos_funcionarios = string_todos_funcionarios + "Nome do funcionario: " + funcionario["nome"] + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "CPF do funcionario: " + str(funcionario["cpf"]) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "Telefone do funcionario: " + funcionario["telefone"] + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "Salario: " + funcionario[
                "salario"] + '\n\n'

        sg.Popup('Funcionarios Cadastrados', string_todos_funcionarios)

    def mostra_mensagem(self, mensagem: str):
        sg.popup("", mensagem)

    def seleciona_funcionario(self):

        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200, 200), (0, 0)
        size = (18, 1)

        while True:
            try:
                layout = [
                    [sg.Column([[sg.Text('Selecionar Funcionário', font=("Palatino Linotype", 30))]],
                               justification='center', pad=((0, 0), (20, 20)))],
                    [sg.Column([[sg.Text('Digite o CPF do funcionário que deseja selecionar:',
                                         font=("Palatino Linotype", 20), pad=15)]],
                               justification='left')],
                    [sg.Column([[sg.Text('CPF:', font=font, size=size, pad=pad), sg.InputText('', key='cpf')]],
                               justification='left')],
                    [sg.Column([[sg.Button('Confirmar', font=font, size=size, pad=pad)]], justification='center')],
                ]

                self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250, 620),
                                          icon="Imagens\pizza icone.ico").Layout(layout)

                button, values = self.open()
                cpf = values['cpf']
                self.close()

                if int(cpf) <= 0:
                    raise Valor_abaixo_de_zero

                elif len(cpf) < 8:
                    raise Entrada_muito_curta

                elif len(cpf) > 11:
                    raise Entrada_muito_longa
                break
            except ValueError:
                self.mostra_mensagem("Entrada inválida!")
            except Valor_abaixo_de_zero as e:
                self.mostra_mensagem(e)
            except Entrada_muito_curta as e:
                self.mostra_mensagem(e)
            except Entrada_muito_longa as e:
                self.mostra_mensagem(e)

        self.close()
        return cpf

    def escolhe_funcao(self):

        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 10)
        pad = (200, 200), (0, 0)
        size = (18, 1)

        while True:
            layout = [
                [sg.Column([[sg.Text('Selecionar Função do Funcionário', font=("Palatino Linotype", 30))]],
                            justification='center', pad=((0, 0), (20, 20)))],
                [sg.Column([[sg.Text('Qual a função do funcionário que está sendo cadastrado?', font=("Palatino Linotype", 20), pad=15)]],
                            justification='left')],
                [sg.Column([[sg.Button('Atendente', key='1', font=font, size=size, pad=pad)]], justification='center')],
                [sg.Column([[sg.Button('Gerente', key='2', font=font, size=size, pad=pad)]], justification='center')],
                [sg.Column([[sg.Button('Pizzaiolo', key='3', font=font, size=size, pad=pad)]], justification='center')],
                [sg.Column([[sg.Button('Entregador', key='4', font=font, size=size, pad=pad)]], justification='center')],
            ]

            self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1250, 620),
                                      icon="Imagens\pizza icone.ico").Layout(layout)

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

        if button == 0 or button in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao
