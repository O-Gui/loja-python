class Carrinho:
    def __init__(self):
        self.produtos = []
        self.quantidades = []

    def adicionar_produto(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.produtos.append(produto)
            self.quantidades.append(quantidade)
            produto.estoque -= quantidade
            print(f"{quantidade}x {produto.nome} adicionado(s) ao carrinho.")
        else:
            print(f"Estoque insuficiente para {produto.nome}.")

    def calcular_total(self):
        total = 0
        for i in range(len(self.produtos)):
            total += self.produtos[i].preco * self.quantidades[i]
        return total

    def mostrar_carrinho(self):
       if not self.produtos:
        print("Carrinho vazio.")
       else:
        print("Carrinho:")
        for i in range(len(self.produtos)):
            produto = self.produtos[i]
            quantidade = self.quantidades[i]
            print(f"{produto.nome} - R${produto.preco:.2f} x {quantidade}")

    def esvaziar(self):
        self.produtos = []
        self.quantidades = []
