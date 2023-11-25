from excecoes import Entrada_muito_curta, Valor_invalido
import PySimpleGUI as sg


class Tela_Produto:

    def __init__(self):
        self.__window = None

    def init_components(self, lista_pizzas):
        print("componentes visuais iniciados geral")
        sg.ChangeLookAndFeel('DarkBrown1')
        font = ("Palatino Linotype", 30)
        layout = [
            [sg.Column([[sg.Text('Produtos', font=("Palatino Linotype", 60))]],
                       justification='center', pad=((0, 0), (60, 40)))],
            [sg.Column([[sg.Image("Imagens\pizza (1).png", subsample=3)]], justification='center')],
            [sg.Column([[sg.Text('Para onde você quer ir?', font=("Palatino Linotype", 50), pad=30)]],
                       justification='center')],

            [sg.Column([[sg.Listbox(values=lista_pizzas, size=(100, 10))]])],

            [sg.Column([[sg.Button('Cadastrar novo produto', key='1', font=("Palatino Linotype", 20), size=(20, 2),
                                   pad=((0, 0), (0, 0)))], [sg.Button('Ver produto', key='2', font=("Palatino Linotype", 20), size=(20, 2), pad=((0, 0), (50, 0)))]], justification='right')],

        ]

        self.__window = sg.Window('Pizzaria', default_element_size=(40, 1), size=(1920, 1080),
                                  icon="Imagens\pizza icone.ico").Layout(layout)

    def abre_tela(self, lista_pizzas):
        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
        self.init_components(lista_pizzas)
        button, values = self.__window.Read()
        button = int(button)
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

        if button == 0 or button in (None, 'Cancelar'):
            opcao = 0

        print(opcao)
        self.close()
        return opcao

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def pegar_dados_produto(self):
        print("Insira os dados do novo produto:")

        while True:
            try:
                tipo = input("Este produto é uma pizza ou uma bebida? ")
                if tipo.upper() != "PIZZA" and tipo.upper() != "BEBIDA":
                    raise ValueError
                break
            except ValueError:
                print("Resposta invalida! Digite \"Pizza\" ou \"Bebida\".")

        while True:
            try:
                nome = input("Insira o nome do produto: ")
                if len(nome) < 2:
                    raise Entrada_muito_curta
                break
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                preco_compra = float(input("Insira o preço de compra: "))
                if preco_compra <= 0:
                    raise Valor_invalido("acima de 0")
                break
            except ValueError:
                print("Digite um numero.")
            except Valor_invalido as e:
                print(e)

        while True:
            try:
                preco_venda = float(input("Insira o preço de venda: "))
                if preco_venda <= 0:
                    raise Valor_invalido("maior que 0")
                elif preco_venda <= preco_compra:
                    raise Valor_invalido("maior que o valor de compra")
                break

            except ValueError:
                print("Digite um numero.")
            except Valor_invalido as e:
                print(e)

        while True:
            try:
                quantidade = int(input("Insira a quantidade em estoque: "))
                if quantidade <= 0:
                    raise Valor_invalido(" maior que 0")
                break
            except ValueError:
                print("Digite um numero.")
            except Valor_invalido as e:
                print(e)

        return {"tipo": tipo, "nome": nome, "preco_compra": preco_compra, "preco_venda": preco_venda, "quantidade": quantidade}

    def ver_produto(self, dados_produto):

        print("Nome do produto: ", dados_produto["nome"])
        print("Tipo do produto: ", dados_produto["tipo"])
        print("Preco de compra do produto: ", dados_produto["preco_compra"])
        print("Preco de venda do produto: ", dados_produto["preco_venda"])
        print("Quantidade em estoque: ", dados_produto["quantidade"])
        print("\n")

    def escolher_produto(self) -> str:
        nome = input("Digite o nome do produto: ")
        return nome

    def close(self):
        self.__window.Close()




