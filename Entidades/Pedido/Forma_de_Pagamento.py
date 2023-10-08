from enum import Enum

class Forma_de_Pagamento(Enum):
    DINHEIRO = "Dinheiro"
    CARTAO_DEBITO = "Cartão de débito"
    CARTAO_CREDITO = "Cartão de crédito"
    PIX = "Pix"

    def __str__(self):
        return self.value




