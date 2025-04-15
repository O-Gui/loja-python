from Produto import Produto

class Loja:
    def __init__(self):
        self.produtos_disponiveis = [
            Produto("Celular", 1000.0, 10),
            Produto("Notebook", 1500.0, 5),
            Produto("PC Gamer", 2000.0, 11),
            Produto("Teclado", 150.0, 8),
            Produto("Mouse", 100.0, 10)
        ]

    def mostrar_produtos(self):
        print("\nProdutos disponíveis na loja:")
        for i, produto in enumerate(self.produtos_disponiveis):
            print(f"{i + 1}. {produto.nome} - R${produto.preco:.2f} | Estoque: {produto.estoque}")

    def selecionar_produto(self, indice):
        if 0 <= indice < len(self.produtos_disponiveis):
            return self.produtos_disponiveis[indice]
        else:
            return None

    def aplicar_desconto(self, produto, percentual):
        desconto = produto.preco * percentual / 100
        produto.preco -= desconto
