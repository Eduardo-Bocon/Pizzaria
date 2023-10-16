from Entidades.Pessoa.Funcionario.Funcionario import Funcionario


class Gerente(Funcionario):

    def __init__(self, nome, cpf, telefone, salario):
        super().__init__(nome, cpf, telefone, salario)
