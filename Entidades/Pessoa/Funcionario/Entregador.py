from Entidades.Pessoa.Funcionario.Funcionario import Funcionario


class Entregador(Funcionario):
    def __init__(self, salario:float, nome: str, cpf: str, telefone: str):
        super().__init__(salario=salario, nome=nome, cpf=cpf, telefone=telefone)

