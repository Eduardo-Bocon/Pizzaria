class Entrada_muito_curta(Exception):
    def __init__(self):
        self.mensagem = "Entrada muito curta!"
        super().__init__(self.mensagem)

class Valor_invalido(Exception):
    def __init__(self, valores_validos):
        self.mensagem = "Valor invalido! Os valores validos são: {}"
        super().__init__(self.mensagem.format(valores_validos))

class Produto_ja_cadastrado(Exception):
    def __init__(self, produto):
        self.mensagem = "O produto {} já existe"
        super().__init__(self.mensagem.format(produto))