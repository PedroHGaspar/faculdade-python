print("Bem-vindos à loja de Marmitas do Pedro Gaspar =]")

print("\nMenu:")
print("1. Bifão Acebolado (BA) - Tamanho P: R$20, M: R$25, G: R$30")
print("2. Filé de Frango (FF) - Tamanho P: R$17, M: R$21, G: R$26")

# declara como variavel global
total_pedido = 0

while True:
    sabor = input("\nDigite o sabor (BA/FF): ").strip().upper()

    if sabor not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente.")
        continue  # volta inicio loop

    # Input do tamanho
    tamanho = input("Digite o tamanho (P/M/G): ").strip().upper()

    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue  # volta inicio loop

    # preço de acordo com tamanho e sabor
    if sabor == "BA":
        if tamanho == "P":
            preco = 20
        elif tamanho == "M":
            preco = 25
        elif tamanho == "G":
            preco = 30
    elif sabor == "FF":
        if tamanho == "P":
            preco = 17
        elif tamanho == "M":
            preco = 21
        elif tamanho == "G":
            preco = 26

    # add preço do pedido
    total_pedido += preco
    print(f"\nPedido confirmado: {sabor} - Tamanho {tamanho}. Preço: R${preco}")

    # pergunta se quer fazer outro pedido
    mais_pedido = input("\nDeseja pedir mais alguma coisa? (s/n): ").strip().lower()
    if mais_pedido != "s":
        break  # fim loop

# output terminal
print(f"\nTotal do pedido: R${total_pedido}")