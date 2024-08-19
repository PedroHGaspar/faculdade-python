print("Bem-vindos a loja do Pedro Gaspar =]")

valorDoPedido = float(input("Digite o valor do pedido: R$ "))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))

# elif = elseif
if quantidadeParcelas < 4:
    juros = 0 / 100
elif 4 <= quantidadeParcelas < 6:
    juros = 4 / 100
elif 6 <= quantidadeParcelas < 9:
    juros = 8 / 100
elif 9 <= quantidadeParcelas < 13:
    juros = 16 / 100
else:
    juros = 32 / 100

# calcular o valor da parcela e o valor total parcelado
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas


# prints no console dos resultados
print(f"Parcelamento com juros de {juros * 100:.0f}%:")
print(f"Valor da Parcela: R$ {valorDaParcela:.2f}")
print(f"Valor Total Parcelado: R$ {valorTotalParcelado:.2f}")


# achei python legal, vou aprofundar mais. Parece ser mais simples do que o js, mesmo que a lógica seja a "mesma".
