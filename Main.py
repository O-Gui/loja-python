from Loja import Loja
from Carrinho import Carrinho

def main():
    loja = Loja()
    carrinho = Carrinho()

    while True:
        print("\n===== MENU DA LOJA =====")
        print("1. Ver produtos disponíveis")
        print("2. Adicionar produto ao carrinho")
        print("3. Ver carrinho")
        print("4. Finalizar compra")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("")
            print("")
            loja.mostrar_produtos()

        elif opcao == "2":
            loja.mostrar_produtos()
            try:
                print("")
                print("")
                escolha = int(input("Digite o número do produto que deseja adicionar: ")) - 1
                produto = loja.selecionar_produto(escolha)
                if produto:
                    quantidade = int(input(f"Quantos '{produto.nome}' deseja adicionar? "))
                    carrinho.adicionar_produto(produto, quantidade)
                else:
                    print("")
                    print("")
                    print("Produto inválido.")
            except ValueError:
                print("Entrada inválida!")

        elif opcao == "3":
            print("")
            print("")
            carrinho.mostrar_carrinho()

        elif opcao == "4":
            total = carrinho.calcular_total()
            if total == 0:
                print("")
                print("")
                print("Carrinho vazio. Adicione itens antes de finalizar.")
                continue

            print("")
            print("")
            print(f"Total da compra: R${total:.2f}")
            print("Formas de pagamento disponíveis:")
            print("1. Cartão")
            print("2. Pix (10% de desconto)")
            metodo = input("Escolha o método de pagamento: ")

            if metodo == "2":
                total *= 0.9
                print("")
                print("")
                print(f"Desconto aplicado! Novo total: R${total:.2f}")

            try:
                confirmacao = float(input(f"Digite o valor exato para confirmar o pagamento: R${total:.2f}\nR$"))
                if confirmacao == round(total, 2):
                    print("\nPagamento aprovado!")
                    carrinho.esvaziar()
                else:
                    print("\nValor incorreto. Pagamento não autorizado.")
            except ValueError:
                print("\nValor inválido!")

        elif opcao == "5":
            print("")
            print("")
            print("Saindo da loja...")
            break

        else:
            print("")
            print("")
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
