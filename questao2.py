print('-' * 7 + 'Bem-Vindo a Pizzaria do Riann Vieira de Souza' + '-' * 11)
print('-' * 25 + 'Cardapio' + '-' * 30)
print('-' * 63)
print('-' * 4 + ' | Tamanho  |  Pizza Salgada (PS)  |  Pizza Doce (PD) | ' + '-' * 3)
print('-' * 4 + ' |     P    |      R$ 30.00        |    R$ 34.00      | ' + '-' * 3)
print('-' * 4 + ' |     M    |      R$ 45.00        |    R$ 48.00      | ' + '-' * 3)
print('-' * 4 + ' |     G    |      R$ 60.00        |    R$ 66.00      | ' + '-' * 3)
print('-' * 63)
# menu dos cardapio


valortotal = 0

# loop com as condições
while True:
    sabor = str(input("Informe o sabor desejado: (PS/PD)"))
    sabor = sabor.upper()

    if sabor != "PS" and sabor != "PD":
        print("Sabor inválido. Tente novamente")
        continue

    tamanho = str(input("Informe o tamanho desejado: (P/M/G) "))
    tamanho = tamanho.upper()

    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente")
        continue
    
# processamento do pedido
    if sabor == "PS":
        if tamanho == "P":
            valortotal += 30
            print(
                f"Você pediu uma Pizza salgada no tamanho P: R$ {valortotal:.2f}")
        elif tamanho == "M":
            valortotal += 45
            print(
                f"Você pediu uma Pizza salgada no tamanho M: R$ {valortotal:.2f}")
        else:
            valortotal += 60
            print(
                f"Você pediu uma Pizza salgada no tamanho G: R$ {valortotal:.2f}")

    if sabor == "PD":
        if tamanho == "P":
            valortotal += 34
            print(
                f"Você pediu uma Pizza doce no tamanho P: R$ {valortotal:.2f}")
        elif tamanho == "M":
            valortotal += 48
            print(
                f"Você pediu uma Pizza doce no tamanho M: R$ {valortotal:.2f}")
        else:
            valortotal += 66
            print(
                f"Você pediu uma Pizza doce no tamanho G: R$ {valortotal:.2f}")

    proximopedido = str(input("Deseja pedir mais alguma coisa? (SIM/NAO)"))
    proximopedido = proximopedido.upper()
#pergunta se deseja algo mais. Se sim, retorna ao processamento do pedido, se não, encerra com o valor total
    if proximopedido == "NÃO" or proximopedido == "NAO":
        break

print(f"Valor pedido total: R$ {valortotal:.2f}")
#valor acumulado do pedido