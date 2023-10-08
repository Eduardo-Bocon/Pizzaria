from enum import Enum


class Sabor(Enum):

    CALABRESA = "Calabresa"
    CALABRESA_CEBOLA = "Calabresa com cebola"
    QUATRO_QUEIJOS = "4 Queijos"
    PORTUGUESA = "Portuguesa"
    MUCARELA = "Muçarela"
    MARGUERITA = "Marguerita"
    FRANGO_CATUPIRY = "Frango com catupiry"
    NAPOLITANA = "Napolitana"

    def __str__(self):
        return self.value
