import csv

# with open("new_file.txt", "a") as f:
#     for i in range(10):
#         f.write("This is a test\n")


def cadastro():
    usuarios = []
    continua = "S"

    while continua.capitalize() == "S":
        pessoa = {}
        pessoa["nome"] = input("Nome: ")
        pessoa["email"] = input("Email: ")
        pessoa["senha"] = input("Senha: ")
        usuarios.append(pessoa)
        continua = input("Deseja continuar? (S/N)")

    return usuarios


def exportaCSV(usuarios):
    with open("Users.csv", "w", newline="") as saida_csv:
        cabecalho = ["nome", "email", "senha"]
        writer = csv.DictWriter(saida_csv, delimiter=";", fieldnames=cabecalho)
        writer.writeheader()
        writer.writerows(usuarios)


usuarios = cadastro()
exportaCSV(usuarios)
print("Exportacao Concluida Com Sucesso")
