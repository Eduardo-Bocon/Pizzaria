from DAOs.dao import DAO
from Entidades.Pessoa.Funcionario import Atendente, Entregador, Gerente, Pizzaiolo


class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario):
        print("Chegou na função de add")
        print(funcionario.cpf)
        if isinstance(funcionario.cpf, str):
            print("Adicionou")
            super().add(funcionario.cpf, funcionario)

    def update(self, funcionario):
        if (funcionario is not None) and (isinstance(funcionario, Atendente.Atendente) or isinstance(funcionario, Entregador.Entregador) or isinstance(funcionario, Gerente.Gerente) or isinstance(funcionario, Pizzaiolo.Pizzaiolo)) and isinstance(funcionario.cpf, str):
            super().update(funcionario.cpf, funcionario)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)