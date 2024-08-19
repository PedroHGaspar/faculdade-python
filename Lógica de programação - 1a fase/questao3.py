# Nome completo do desenvolvedor
print("Bem-vindos à Fábrica de Camisetas do Pedro Gaspar =]")

def escolha_modelo():
    # escolhe o modelo da camiseta
    while True:
        modelo = (
            input("Digite o modelo da camiseta (MCS/MLS/MCE/MLE): ").strip().upper()
        )
        if modelo == "MCS":
            return 10.80
        elif modelo == "MLS":
            return 20.10
        elif modelo == "MCE":
            return 20.90
        elif modelo == "MLE":
            return 30.20
        else:
            print("Modelo inválido. Tente novamente.")

def num_camisetas():
    # numero de camisetas com o desconto aplicado
    while True:
        try:
            quantidade = int(input("Digite o número de camisetas: "))
            if quantidade > 20000:
                print("Número de camisetas acima do permitido. Tente novamente.")
            elif quantidade >= 2000:
                desconto = 0.12
                return quantidade, (1 - desconto)
            elif quantidade >= 200:
                desconto = 0.07
                return quantidade, (1 - desconto)
            elif quantidade >= 20:
                desconto = 0.05
                return quantidade, (1 - desconto)
            elif quantidade >= 0:
                return quantidade, 1
            else:
                print("Número de camisetas inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def frete():
    # escolher tipo de frete e seu valor
    while True:
        tipo_frete = input(
            "Digite o tipo de frete (1 para transportadora, 2 para Sedex, 3 para retirar na fábrica): "
        ).strip()
        if tipo_frete == "1":
            return 100
        elif tipo_frete == "2":
            return 200
        elif tipo_frete == "3":
            return 3
        else:
            print("Opção de frete inválida. Tente novamente.")

# funcao principal
if __name__ == "__main__":
    valor_modelo = escolha_modelo()
    quantidade, desconto = num_camisetas()
    valor_frete = frete()

    if quantidade > 20000:
        print("Número de camisetas acima do limite permitido. Pedido não aceito.")
    else:
        # calcula valor + desconto + frete
        total = (valor_modelo * quantidade * desconto) + valor_frete
        print(f"\nPedido confirmado:")
        print(f"Modelo escolhido: {valor_modelo:.2f} reais")
        print(f"Número de camisetas: {quantidade}")
        print(f"Desconto aplicado: {int((1 - desconto) * 100)}%")
        print(f"Frete: {valor_frete} reais")
        print(f"Total a pagar: {total:.2f} reais")
