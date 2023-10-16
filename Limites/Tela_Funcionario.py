from excecoes import Entrada_muito_curta, Entrada_muito_longa, Valor_abaixo_de_zero


class Tela_Funcionario():

    def pega_dados_funcionario(self):
        print("Insira os dados do funcionário.")

        while True:
            try:
                nome = input("Insira o nome do funcionário: ")
                if len(nome) < 4:
                    raise Entrada_muito_curta
                break
            except ValueError:
                print("Entrada inválida!")
            except Entrada_muito_curta as e:
                print(e)

        while True:
            try:
                telefone = input("Insira o telefone do funcionário: ")

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
                cpf = input("Insira o CPF do funcionário: ")

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

        while True:
            try:
                salario = input("Insira o salário do funcionário: ")

                if int(salario) <= 0:
                    raise Valor_abaixo_de_zero
                break
            except ValueError:
                print("Entrada inválida!")

        return {"nome": nome, "telefone": telefone, "cpf": cpf, "salario": salario}

    def mostra_funcionarios(self, dados_funcionario):
        print("Nome do funcionário: ", dados_funcionario["nome"])
        print("CPF do funcionário: ", dados_funcionario["cpf"])
        print("Telefone do funcionário: ", dados_funcionario["telefone"])
        print("Salário do funcionário: ", dados_funcionario["salario"])
        print("\n")

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def seleciona_funcionario(self):
        while True:
            try:
                cpf = input("Insira o CPF do funcionário que deseja selecionar: ")

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
    
    def escolhe_funcao(self):
        print("1 - Atendente; 2 - Gerente; 3 - Pizzaiolo, 4 - Entregador")

        while True:
            try:
                funcao = int(input("Insira o número da função do funcionário:"))
                if funcao < 1 or funcao > 4:
                    raise ValueError
                return funcao
            except ValueError:
                print("Valor inválido, insira um valor entre 1 e 4!")

    def abre_tela(self):
        print("---- Tela Funcionários ----")
        print("Opcões:")
        print("1 - Cadastrar Funcionário")
        print("2 - Modificar Funcionário")
        print("3 - Deletar Funcionário")
        print("4 - Ver Clientes")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("O que deseja fazer? "))
                print("")
                if opcao < 0 or opcao > 4:
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor inválido, insira um valor entre 0 e 4!")
