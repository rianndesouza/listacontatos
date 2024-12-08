print("Bem-vindos à madeireira do Lenhador Riann Vieira de Souza")

#tipos de madeiras e valores são armazenados aqui
precos_madeira = {
    "PIN": 150.40,  
    "PER": 170.20,  
    "MOG": 190.90,  
    "IPE": 210.10,  
    "IMB": 220.70   
}

def escolha_tipo():
    try:
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")
        
        escolha = input("Escolha o tipo de madeira (PIN, PER, MOG, IPE, IMB): ").upper()

        while escolha not in precos_madeira: #usei o not in, onde verifica se a escolha do usuario esta armazenado na biblioteca la em cima
            print("Escolha inválida. Entre com o modelo novamente.")
            escolha = input("Escolha o tipo de madeira (PIN, PER, MOG, IPE, IMB): ").upper()

        return escolha, precos_madeira[escolha]

    except Exception as e:
        print(f"Erro: {e}. Tente novamente.")
        return escolha_tipo()

tipo_madeira, valor_madeira = escolha_tipo()
print(f"Você escolheu: {tipo_madeira} - Valor: R$ {valor_madeira:.2f}")

def qtd_toras():
    try:
        while True:
            qtd_toras = int(input("Entre com a quantidade de toras (m³): "))
            desconto = 0

            if qtd_toras < 100:
                print(f"Você escolheu: {qtd_toras} toras")
                break
            elif 100 <= qtd_toras < 500:
                desconto = 4 / 100
                print(f"Você escolheu: {qtd_toras} toras\nDesconto: {desconto * 100}%")
                break
            elif 500 <= qtd_toras < 1000:
                desconto = 9 / 100
                print(f"Você escolheu: {qtd_toras} toras\nDesconto: {desconto * 100}%")
                break
            elif 1000 <= qtd_toras < 2000:
                desconto = 16 / 100
                print(f"Você escolheu: {qtd_toras} toras\nDesconto: {desconto * 100}%")
                break
            elif qtd_toras > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras. Por favor, informe uma quantidade válida.")
            else:
                break

        return qtd_toras, desconto

    except ValueError:
        print("Erro: Entre com um valor numérico válido para a quantidade de toras.") #uso do except para caso o valor informado não seja numerico
        return qtd_toras()

qtd_toras, desconto = qtd_toras()

def transporte():
    try:
        print("1 - Transporte Rodoviário: R$ 1000.00")
        print("2 - Transporte Ferroviário: R$ 2000.00")
        print("3 - Transporte Hidroviário: R$ 2500.00")
        
        opcao = int(input("Escolha o tipo de transporte (1, 2, 3): "))

        precos_transporte = {
            1: 1000.00,
            2: 2000.00,
            3: 2500.00
        }

        while opcao not in precos_transporte:
            print("Escolha de transporte inválida.")
            opcao = int(input("Escolha o tipo de transporte (1, 2, 3): "))

        return precos_transporte[opcao]

    except ValueError:
        print("Erro: Escolha inválida. Entre com um número para o tipo de transporte.")
        return transporte()

valor_transporte = transporte()

#calculo final e print
valor_final = valor_madeira * qtd_toras * (1 - desconto) + valor_transporte
print(f"Valor total: R$ {valor_final:.2f}")
