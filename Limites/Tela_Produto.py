from excecoes import Entrada_muito_curta, Valor_invalido


class Tela_Produto:

    def abre_tela(self):
        print("---- Tela Produtos ----")
        print("Opcões:")
        print("1 - Cadastrar Produto")
        print("2 - Modificar Produto")
        print("3 - Ver Produtos")
        print("4 - Deletar Produto")
        print("0 - Retornar")

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




