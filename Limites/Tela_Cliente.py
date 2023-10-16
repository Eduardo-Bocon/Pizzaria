
from excecoes import Entrada_muito_curta, Entrada_muito_longa, Valor_abaixo_de_zero


class Tela_Cliente():

    def pega_dados_cliente(self):
        print("Insira os dados do cliente:")

        while True:
            try:
                nome = input("Insira o nome do cliente: ")
                if len(nome) < 4:
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

        endereco = self.pega_endereco()

        return {"nome": nome, "telefone": telefone, "cpf": cpf, "endereco": endereco}
    
    def pega_endereco(self):
        print("Insira seu endereço completo:")

        while True:
            try:
                numero = input("Insira o número do endereço:")
                if numero <= 0:
                    raise Valor_abaixo_de_zero
                break
            except ValueError:
                print("Inválido! Insira apenas números!")
            except Valor_abaixo_de_zero as e:
                print(e)

        while True:
            try:
                rua = input("Insira a rua do endereço: ")
                if len(rua) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                bairro = input("Insira o bairro do endereço: ")
                if len(bairro) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                cidade = input("Insira a cidade do endereço: ")
                if len(cidade) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                cep = input("Insira o CEP do endereço: ")

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

        return {"numero": numero, "rua": rua, "bairro": bairro, "cidade": cidade, "cep": cep}
    
    def mostra_clientes(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("CPF do cliente: ", dados_cliente["cpf"])
        print("Telefone do cliente: ", dados_cliente["telefone"])
        print("Cidade do endereço do cliente: ", dados_cliente["cidade"])
        print("\n")

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def seleciona_cliente(self):
        while True:
            try:
                cpf = input("Insira o CPF do cliente que deseja selecionar: ")

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

        return cpf

    def abre_tela(self):
        print("---- Tela Clientes ----")
        print("Opcões:")
        print("1 - Cadastrar Cliente")
        print("2 - Modificar Cliente")
        print("3 - Deletar Cliente")
        print("4 - Ver Clientes")
        print("5 - Ver Clientes fiéis")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                if opcao < 0 or opcao > 5:
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor inválido, insira um valor entre 0 e 5!")
