from DAOs.produto_dao import ProdutoDAO
from Entidades.Produtos import Produto
from Entidades.Produtos.Bebida import Bebida
from Entidades.Produtos.Pizza import Pizza
from Limites.Tela_Produto import Tela_Produto
from excecoes import Produto_ja_cadastrado


class ControladorProduto():

    def __init__(self, controlador_pizzaria):
        self.__tela = Tela_Produto()
        self.__produto_DAO = ProdutoDAO()
        self.__controlador_pizzaria = controlador_pizzaria

    def retornar(self):
        self.__controlador_pizzaria.abre_tela_geral()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_produto, 2: self.modificar_produto, 3: self.deletar_produto,
                        4: self.ver_produtos,
                        0: self.retornar}

        while 1:
            lista_opcoes[self.__tela.abre_tela(self.pegar_pizzas())]()

    def cadastrar_produto(self):
        dados_novo_produto = self.__tela.pegar_dados_produto()
        nome = dados_novo_produto["nome"]
        novo_produto = self.pegar_produto(nome)

        try:
            if novo_produto is None:
                if dados_novo_produto["tipo"].upper() == "PIZZA":
                    novo_produto = Pizza(preco_venda=dados_novo_produto["preco_venda"],
                                         preco_compra=dados_novo_produto["preco_compra"],
                                         quantidade=dados_novo_produto["quantidade"], nome=dados_novo_produto["nome"])
                elif dados_novo_produto["tipo"].upper() == "BEBIDA":
                    novo_produto = Bebida(preco_venda=dados_novo_produto["preco_venda"],
                                          preco_compra=dados_novo_produto["preco_compra"],
                                          quantidade=dados_novo_produto["quantidade"], nome=dados_novo_produto["nome"])
                self.__produto_DAO.add(novo_produto)
            else:
                raise Produto_ja_cadastrado(nome)
        except Produto_ja_cadastrado as e:
            self.__tela.mostra_mensagem(e)

    def modificar_produto(self):
        self.ver_produtos()

        if not self.__produto_DAO.get_all():
            self.__tela.mostra_mensagem("Nenhum produto cadastrado!")

        else:
            nome = self.__tela.escolher_produto()
            produto = self.pegar_produto(nome)

            if (produto is not None):

                if isinstance(produto, Pizza):
                    novos_dados_produto = self.__tela.pegar_dados_produto(
                        {"tipo":"Pizza", "nome": produto.nome, "preco_venda": produto.preco_venda, "preco_compra": produto.preco_compra,
                         "quantidade": produto.quantidade})
                elif isinstance(produto, Bebida):
                    novos_dados_produto = self.__tela.pegar_dados_produto(
                        {"tipo": "Bebida", "nome": produto.nome, "preco_venda": produto.preco_venda,
                         "preco_compra": produto.preco_compra,
                         "quantidade": produto.quantidade})



                produto.nome = novos_dados_produto["nome"]
                produto.preco_venda = novos_dados_produto["preco_venda"]
                produto.preco_compra = novos_dados_produto["preco_compra"]
                produto.quantidade = novos_dados_produto["quantidade"]

                self.__produto_DAO.update(produto)

                self.ver_produtos()
            else:
                self.__tela.mostra_mensagem("Erro: produto não existente")

    def ver_produtos(self):
        if not self.__produto_DAO.get_all():
            self.__tela.mostra_mensagem("Nenhum produto cadastrado.")

        else:
            lista_produtos = []
            for produto in self.__produto_DAO.get_all():
                if isinstance(produto, Pizza):
                    lista_produtos.append({"nome": produto.nome, "tipo": "Pizza", "preco_compra": produto.preco_compra,
                                           "preco_venda": produto.preco_venda, "quantidade": produto.quantidade})
                elif isinstance(produto, Bebida):
                    lista_produtos.append(
                        {"nome": produto.nome, "tipo": "Bebida", "preco_compra": produto.preco_compra,
                         "preco_venda": produto.preco_venda, "quantidade": produto.quantidade})
            self.__tela.ver_produtos(lista_produtos)

    def pegar_produto(self, nome: str) -> Produto:
        for produto in self.__produto_DAO.get_all():
            if produto.nome == nome:
                return produto
        return None

    def deletar_produto(self):
        self.ver_produtos()

        if not self.__produto_DAO.get_all():
            self.__tela.mostra_mensagem("Nenhum produto cadastrado!")

        else:
            nome = self.__tela.escolher_produto()
            produto = self.pegar_produto(nome)

            if produto is not None:
                self.__produto_DAO.remove(produto.nome)
                self.ver_produtos()
            else:
                self.__tela.mostra_mensagem("Erro: produto não existente")

    def pegar_pizzas(self):
        pizzas = list()
        for produto in self.__produto_DAO.get_all():
            if isinstance(produto, Pizza):
                pizzas.append(produto.nome)
        return pizzas

    def pegar_bebidas(self):
        bebidas = list()
        for produto in self.__produto_DAO.get_all():
            if isinstance(produto, Bebida):
                bebidas.append(produto.nome)
        return bebidas

    def pegar_produtos(self):
        produtos = list()
        for produto in self.__produto_DAO.get_all():
            produtos.append(produto.nome)
        return produtos
