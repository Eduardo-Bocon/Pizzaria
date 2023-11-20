import PySimpleGUI as sg
from excecoes import Entrada_muito_curta, Entrada_muito_longa, Valor_abaixo_de_zero


class Tela_Cliente():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        print("componentes visuais iniciados cliente")
        sg.ChangeLookAndFeel('DarkRed1')

        layout = [
            [sg.Text('---- Tela Clientes ----')],
            [sg.Button('Cadastrar Cliente', key='1')],
            [sg.Button('Modificar Cliente', key='2')],
            [sg.Button('Deletar Cliente', key='3')],
            [sg.Button('Ver Clientes', key='4')],
            [sg.Button('Ver Clientes Fiéis', key='5')],
            [sg.Button('Retornar', key='0')],
            [sg.Submit("Selecionar"), sg.Cancel("Retornar")]
        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40,1), size=(1000,500)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [
            [sg.Text('-------- Dados do Cliente ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Pizzaria').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        cpf = values['cpf']

        while True:
            try:
                nome = input("Insira o nome do cliente: ")
                if len(nome) < 3:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                telefone = input("Insira o telefone do cliente: ")

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
                cpf = input("Insira o CPF do cliente: ")

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
        sg.ChangeLookAndFeel('DarkRed1')
        layout = [
            [sg.Text('-------- Endereço ----------', font=("Helvica", 25))],
            [sg.Text('numero:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Text('rua:', size=(15, 1)), sg.InputText('', key='rua')],
            [sg.Text('bairro:', size=(15, 1)), sg.InputText('', key='bairro')],
            [sg.Text('cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
            [sg.Text('cep:', size=(15, 1)), sg.InputText('', key='cep')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        numero = values['numero']
        rua = values['rua']
        bairro = values['bairro']
        cidade = values['cidade']
        cep = values['cep']

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

        sg.Popup('-------- Clientes Cadastrados ----------', string_todos_clientes)

    def mostra_mensagem(self, mensagem: str):
        sg.popup("", mensagem)

    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkRed1')
        while True:
            try:
                layout = [
                    [sg.Text('-------- SELECIONAR AMIGO ----------', font=("Helvica", 25))],
                    [sg.Text('Digite o CPF do amigo que deseja selecionar:', font=("Helvica", 15))],
                    [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
                self.__window = sg.Window('Seleciona amigo').Layout(layout)
                
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
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0

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
