from Entidades.Pessoa.Pessoa import Pessoa
from Entidades.Pessoa.Cliente.Endereco import Endereco


class Cliente(Pessoa):

    def __init__(self, nome:str, cpf:str, telefone:str, numero: int, rua: str, bairro: str, cidade: str, cep: str):
        super().__init__(nome=nome, cpf=cpf, telefone=telefone)
        self.__quantidade_pedidos = 0
        self.__endereco = Endereco(numero=numero, rua=rua, bairro=bairro, cidade=cidade, cep=cep)

    @property
    def quantidade_pedidos(self):
        return self.__quantidade_pedidos
    
    @quantidade_pedidos.setter
    def quantidade_pedidos(self, quantidade_pedidos):
        if isinstance(quantidade_pedidos, int):
            self.__quantidade_pedidos = quantidade_pedidos

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, Endereco):
            self.__endereco = endereco


