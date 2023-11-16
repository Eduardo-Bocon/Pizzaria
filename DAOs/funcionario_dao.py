from DAOs.dao import DAO
from Entidades.Pessoa.Funcionario import Atendente, Entregador, Gerente, Pizzaiolo


class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario):
        if((funcionario is not None) and (isinstance(funcionario, Atendente) or isinstance(funcionario, Entregador) or isinstance(funcionario, Gerente) or isinstance(funcionario, Pizzaiolo)) and isinstance(funcionario.cpf, str)):
            super().add(funcionario.cpf, funcionario)

    def update(self, funcionario):
        if((funcionario is not None) and (isinstance(funcionario, Atendente) or isinstance(funcionario, Entregador) or isinstance(funcionario, Gerente) or isinstance(funcionario, Pizzaiolo)) and isinstance(funcionario.cpf, str)):
            super().update(funcionario.cpf, funcionario)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)