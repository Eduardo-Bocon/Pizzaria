class Tela_Geral():

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