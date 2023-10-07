
class Estoque:
    def __init__(self):
        self.queijo_kg = 0
        self.tomates_kg = 0
        self.calabresa_kg = 0
        self.frango_kg = 0
        self.molho_tomate_saco = 0
        self.cebola_kg = 0
        self.COCA = 0
        self.GUARANA = 0
        self.SPRITE = 0
        self.AGUA = 0
        self.AGUA_GAS = 0
        self.VINHO = 0
        self.CERVEJA = 0

    @property
    def queijo_kg(self):
        return self.queijo_kg

    @property
    def tomates_kg(self):
        return self.tomates_kg