lista_produtos = []
valor_total = 0
while True:
    print("\n----MENU----:")
    print("1. Adicionar Produto")
    print("2. Exibir Lista de Produtos")
    print("3. Atualizar")
    print("4.Remover")
    print("5. Sair")

    escolha = input("Escolha a opção desejada: ")

    if escolha == '1':
        
        produto = {}
        produto['nome'] = input("Digite o nome do produto: ").upper()
        produto['quantidade'] = int(input("Digite a quantidade do produto: "))
        produto['valor'] = float(input("Digite o valor do produto: "))
        produto['total'] = produto['quantidade'] * produto['valor']
        lista_produtos.append(produto)
        valor_total = produto['total'] + valor_total
        print("Produto adicionado com sucesso!")
        print()
        print(f"O valor total dos produtos adicionados é {valor_total}")
        

    elif escolha == '2':
        print("*** LISTA DE PRODUTOS CADASTRADOS ***")
        print("--------------------------------------")
        print("FRUTAS CADASTRADAS:")
        for i, produto in enumerate(lista_produtos):
                print(f"\nProduto {i}:")
                for chave, valor in produto.items():
                    print(f"{chave}: {valor}")
        print(f"O valor total dos produtos cadastrados até o momento é {valor_total}")
    elif escolha == '3':
        
        indice = int(input("Digite o número do produto que deseja editar: ")) - 1
        if 0 <= indice < len(lista_produtos):
                produto = lista_produtos[indice]
                produto['nome'] = input("Digite o novo nome do produto: ")
                produto['quantidade'] = int(input("Digite a nova quantidade do produto: "))
                produto['valor'] = float(input("Digite o novo valor do produto: "))
                print("Produto editado com sucesso!")
        else:
                print("Índice inválido. Tente novamente.")
    elif escolha == '4':
        
        indice = int(input("Digite o número do produto que deseja remover: ")) - 1
        if 0 <= indice < len(lista_produtos):
                remover = lista_produtos.pop(indice)
                print(f"Produto removido com sucesso: {remover}")
        else:
                print("Índice inválido. Tente novamente.")
    elif escolha == '5':
        print("Até mais! Finalizando...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        
         

        



        






      