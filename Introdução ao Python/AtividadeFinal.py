import csv


def menu():
    print("\n===Sistema de Inventario===")
    op = input(
        "1 - Adicionar Item\n2 - Remover Item\n3 - Listar Itens\n4 - Exportar em CSV\n5 - Sair\n")
    return op


def Adicionar(identificador):
    produto = {}
    produto["nome"] = input("\nDescrição: ").capitalize()
    produto["preco"] = input("Preço: ")
    produto["id"] = identificador
    print("Item Adicionado Com Sucesso")
    return produto


def Listar(lista):
    print("\nID | Preço | Descrição")
    for item in lista:
        print(
            f"{item.get('id')} | {float(item.get('preco')):.2f} | {item.get('nome')}")


def Remover(lista):
    codigo = input("\nInsira o ID do código a ser removido: ")
    itemSelecionado = None
    for item in lista:
        if item.get("id") == int(codigo):
            itemSelecionado = item
            break
    if itemSelecionado != None:
        print("\nID | Preço | Descrição")
        print(
            f"{itemSelecionado.get('id')} | {float(itemSelecionado.get('preco')):.2f} | {itemSelecionado.get('nome')}")
        if input("Tem certeza que deseja remover o item? (S/N)\n").capitalize() == "S":
            lista.remove(itemSelecionado)
            print("O Item Foi Removido Com Sucesso")
        else:
            print("O Item Não Será Removido")
            return
    else:
        print(f"Item de Código {codigo} Não Existe")


def Exportar(saida):
    with open("Inventario.csv", "w", newline="") as saida_csv:
        cabecalho = ["id", "preco", "nome"]
        writer = csv.DictWriter(saida_csv, delimiter=";", fieldnames=cabecalho)
        writer.writeheader()
        writer.writerows(saida)


identificador = 0
inventario = []
op = 0
while True:
    op = int(menu())
    if op == 1:
        inventario.append(Adicionar(identificador))
        identificador += 1
    elif op == 2:
        Remover(inventario)
    elif op == 3:
        Listar(inventario)
    elif op == 4:
        Exportar(inventario)
    elif op == 5:
        quit()
    else:
        print("Insira uma opção válida")
