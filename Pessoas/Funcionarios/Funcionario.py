from Pessoas.Pessoa import Pessoa
from abc import ABC, abstractmethod


class Funcionario(Pessoa, ABC):

    def __init__(self):
        super.__init__()

