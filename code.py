# Exemplo de um repertório simples em Python

# Função para adicionar um item ao repertório
def adicionar_item(repertorio, chave, valor):
    repertorio[chave] = valor
    print(f"Item '{chave}' adicionado ao repertório.")

# Função para remover um item do repertório
def remover_item(repertorio, chave):
    if chave in repertorio:
        del repertorio[chave]
        print(f"Item '{chave}' removido do repertório.")
    else:
        print(f"Item '{chave}' não encontrado no repertório.")

# Função para exibir o repertório
def exibir_repertorio(repertorio):
    if not repertorio:
        print("O repertório está vazio.")
    else:
        print("Conteúdo do repertório:")
        for chave, valor in repertorio.items():
            print(f"  '{chave}': '{valor}'")

# Função para buscar um item no repertório
def buscar_item(repertorio, chave):
    if chave in repertorio:
        print(f"O valor para '{chave}' é '{repertorio[chave]}'.")
    else:
        print(f"Item '{chave}' não encontrado no repertório.")

# Inicializando o repertório (um dicionário em Python)
meu_repertorio = {}

# Menu de opções
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir repertório")
    print("4. Buscar item")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        adicionar_item(meu_repertorio, chave, valor)
    elif opcao == '2':
        chave = input("Digite a chave a ser removida: ")
        remover_item(meu_repertorio, chave)
    elif opcao == '3':
        exibir_repertorio(meu_repertorio)
    elif opcao == '4':
        chave = input("Digite a chave a ser buscada: ")
        buscar_item(meu_repertorio, chave)
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
