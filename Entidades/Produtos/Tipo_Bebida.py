from enum import Enum


class Tipo_Bebida(Enum):

    #refris
    COCA = "Coca-cola"
    GUARANA = "Guaraná"
    SPRITE = "Sprite"
    #aguas
    AGUA = "Água"
    AGUA_GAS = "Água com gás"
    #alcolicos
    VINHO = "Vinho"
    CERVEJA = "Cerveja"


    def __str__(self):
        return self.value

