class Tela_Pizzaria():

    def abre_tela(self):
        print("---- Tela Pizzaria ----")
        print("Opcões:")
        print("1 - Ir para tela dos produtos")
        print("2 - Ir para tela dos clientes")
        print("3 - Ir para tela dos funcionários")
        print("4 - Ir para tela de pedidos")
        print("5 - Ver relatório da pizzaria")
        print("0 - Encerrar programa")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                if opcao < 0 or opcao > 5:
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor invalido. Insira um valor entre 0 e 5.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def ver_relatorio(self, salarios, despesas, receitas, atendente_do_mes):
        print("Atendente do mês: {}".format(atendente_do_mes))
        print("Total de salários: {}".format(salarios))
        print("Total de despesas: {}".format(despesas))
        print("Total de receitas: {}".format(receitas))
        print("Lucro total: {}".format(receitas - despesas))
        