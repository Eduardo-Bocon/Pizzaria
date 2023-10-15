class Tela_Pizzaria():

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
                if opcao < 0 or opcao > 5:
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor invalido. Insira um valor entre 0 e 5.")

    def abre_tela(self):
        print("---- Tela Pizzaria ----")
        print("Opcões:")
        print("1 - Ver atendente do mês")
        print("2 - Ver produto mais vendido")
        print("3 - Ver total dos salários")
        print("4 - Ver despesas")
        print("5 - Ver receita")
        print("6 - Ver lucro total")
        print("0 - Encerrar programa")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                if opcao < 0 or opcao > 6:
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor invalido. Insira um valor entre 0 e 6.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def atendente_do_mes(self, atendente_do_mes):
        print("Atendente do mês: {}".format(atendente_do_mes))

    def produto_mais_vendido(self, produto_mais_vendido):
        print("Produto mais vendido do mês: {}".format(produto_mais_vendido))  

    def salarios(self, salarios):
        print("Total de salários: {}".format(salarios))

    def despesas(self, despesas):
        print("Total de despesas: {}".format(despesas))

    def receitas(self, receitas):
        print("Total de receitas: {}".format(receitas))

    def lucro(self, despesas, receitas):
        print("Lucro total: {}".format(receitas - despesas))
        