class Tela_Pedido(): #todo

    def abre_tela(self):
        print("---- Tela Pedidos ----")
        print("Opcões:")
        print("1 - Fazer pedido")
        print("2 - Modificar pedido")
        print("3 - Ver pedidos")
        print("4 - Deletar Pedido")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                if opcao < 0 or opcao > 4:
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor invalido. Insira um valor entre 0 e 4.")

    def fazer_pedido(self):
        pass
    
    def deletar_pedido(self):
        pass

    def modificar_pedido(self):
        pass

    def ver_pedido(self):
        pass

    def mostra_mensagem(self, mensagem: str):
        pass

    def busca_pedido(self, codigo: int):
        pass


