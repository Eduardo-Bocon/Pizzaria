class Tela_Pizzaria():

    def abre_tela(self):
        print("---- Tela Pizzaria ----")
        print("Opcões:")
        print("1 - Ver atendente do mês")
        print("2 - Ver produto mais vendido")
        print("3 - Ver financeiro")
        print("0 - Encerrar programa")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                if opcao < 0 or opcao > 4:
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor invalido. Insira um valor entre 0 e 4.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def atendente_do_mes(self, atendente_do_mes):
        if atendente_do_mes is None:
            print("Não há pedidos com atendentes.")
        else:
            print("Atendente do mês: {}".format(atendente_do_mes))

    def produto_mais_vendido(self, produto_mais_vendido):
        if produto_mais_vendido is None:
            print("Não há pedidos com produtos.")
        else:
            print("Produto mais vendido do mês: {}".format(produto_mais_vendido))

    def mostrar_financeiro(self, salarios, despesas, receitas):
        print("Total de salários: {}".format(salarios))
        print("Total de despesas: {}".format(despesas))
        print("Total de receitas: {}".format(receitas))
        print("Lucro total: {}".format(receitas - despesas))
        print("")

        