class Entrada_muito_curta(Exception):
    def __init__(self):
        self.mensagem = "Entrada muito curta!"
        super().__init__(self.mensagem)

class Valor_abaixo_de_zero(Exception):
    def __init__(self):
        self.mensagem = "Valor inválido, apenas valores acima de zero!"
        super().__init__(*self.mensagem)

class Valor_invalido(Exception):
    def __init__(self, valores_validos):
        self.mensagem = "Valor invalido! Os valores validos são: {}"
        super().__init__(self.mensagem.format(valores_validos))

class Entrada_muito_longa(Exception):
    def __init__(self):
        self.mensagem = "Entrada muito longa!"
        super().__init__(self.mensagem)

class Produto_ja_cadastrado(Exception):
    def __init__(self, produto):
        self.mensagem = "O produto {} já existe"
        super().__init__(self.mensagem.format(produto))

class Pedido_ja_cadastrado(Exception):
    def __init__(self, pedido):
        self.mensagem = "O pedido {} já existe"
        super().__init__(self.mensagem.format(pedido))

class Cliente_ja_cadastrado(Exception):
    def __init__(self, cliente):
        self.mensagem = "O cliente {} já está cadastrado"
        super().__init__(self.mensagem.format(cliente))

class Funcionario_ja_cadastrado(Exception):
    def __init__(self, funcionario):
        self.mensagem = "O funcionario {} já está cadastrado"
        super().__init__(self.mensagem.format(funcionario))

class Forma_de_Pagamento_Invalida(Exception):
    def __init__(self):
        self.mensagem = "Forma de pagamento invalida."
        super().__init__(self.mensagem.format())

class Atendente_nao_encontrado(Exception):
    def __init__(self):
        self.mensagem = "Atendente não encontrado."
        super().__init__(self.mensagem.format())
