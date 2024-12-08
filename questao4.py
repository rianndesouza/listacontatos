print("Bem vindo à lista de contatos de Riann Vieira de Souza")
print('-' * 63)
print('-' * 23 + ' Menu Principal ' + '-' * 23)

lista_contatos = []

def cadastrar_contato():
    print('-' * 63)
    print('-' * 21 + ' Menu Cadastrar Contato ' + '-' * 21)
    try:
        id = int(input("Por favor, informe o Id do contato: "))
    except ValueError:
        print("ID inválido! Use apenas números.")
        return
    nome = input("Por favor, informe o nome do contato: ")
    atividade = input("Por favor, informe a atividade do contato: ")
    telefone = input("Por favor, informe o número do contato: ")
    print('-' * 21 + ' Contato Cadastrado ' + '-' * 21)
    
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    lista_contatos.append(contato.copy())
    print(f"Contato de {nome} cadastrado com sucesso!")

def consultar_contatos():
    while True:
        print('-' * 63)
        print('-' * 21 + ' Menu Consultar Contatos ' + '-' * 21)
        print("\n1. Consultar todos os contatos")
        print("2. Consultar contato por Id")
        print("3. Consultar Contato(s) por atividade")
        print("4. Retornar")
        opção = input("Escolha a opção: ")
        print('-' * 63)
        
        if opção == '1':
            if not lista_contatos:
                print("Nenhum contato cadastrado.")
            else:
                for contato in lista_contatos:
                    print(contato)

        elif opção == '2':
            try:
                id_consulta = int(input("Informe o Id do contato: "))
                contato_encontrado = next(
                    (contato for contato in lista_contatos if contato["id"] == id_consulta), None)
                if contato_encontrado:
                    print(contato_encontrado)
                else:
                    print("Contato não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, informe um número válido.")

        elif opção == '3':
            atividade_consulta = input("Informe a atividade do contato: ")
            contatos_encontrados = [contato for contato in lista_contatos if contato["atividade"].lower() == atividade_consulta.lower()]
            if contatos_encontrados:
                for contato in contatos_encontrados:
                    print(contato)
            else:
                print("Nenhum contato encontrado com essa atividade.")
                
        elif opção == '4':
            return
        else:
            print("Opção inválida.")

def remover_contato():
    print('-' * 63)
    print('-' * 21 + ' Menu Remover Contato ' + '-' * 21)
    while True:
        try:
            id_remover = int(input("Informe o Id do contato que deseja remover: "))
            contato_encontrado = next((contato for contato in lista_contatos if contato["id"] == id_remover), None)
            if contato_encontrado:
                lista_contatos.remove(contato_encontrado)
                print(f"Contato com Id {id_remover} removido com sucesso.")
                break
            else:
                print("Id inválido.")
        except ValueError:
            print("Por favor, entre com um número válido para o ID.")

# Loop principal do menu
while True:
    print("1. Cadastrar contato")
    print("2. Consultar contato")
    print("3. Remover contato")
    print("4. Sair")
    print('-' * 63)
    opção = input("Escolha a opção: ")
    
    if opção == '1':
        cadastrar_contato()
    elif opção == '2':
        consultar_contatos()
    elif opção == '3':
        remover_contato()
    elif opção == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")