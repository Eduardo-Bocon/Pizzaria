class Endereco():

    def __init__(self, numero: int, rua: str, bairro: str, cidade: str, cep: str):
        self.__numero = numero
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def nome(self, cidade):
        self.__cidade = cidade

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep
