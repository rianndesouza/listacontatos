print("Bem-vindo ao Sistema do Riann Vieira de Souza")

# Entrada
valorbase = float(input("Informe o valor base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))

# programa principal
if idade >= 0 and idade <= 19:
    porcentagem = 100 / 100
elif idade > 19 and idade <= 29:
    porcentagem = 150 / 100
elif idade > 29 and idade <= 39:
    porcentagem = 225 / 100
elif idade > 39 and idade <= 49:
    porcentagem = 240 / 100
elif idade > 49 and idade <= 59:
    porcentagem = 350 / 100
else:
    porcentagem = 600 / 100

# calculo valor mensal
valormensal = valorbase * porcentagem

# valor mensal final
print(f"O valor mensal do plano é: R$ {valormensal:.2f}")