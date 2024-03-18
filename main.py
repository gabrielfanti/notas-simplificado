class Nota:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

def adicionar_nota(notas, titulo, descricao):
    nova_nota = Nota(titulo, descricao)
    notas.append(nova_nota)
    print("Nota adicionada com sucesso!")

def exibir_notas(notas):
    if notas:
        print("Suas notas:")
        for i, nota in enumerate(notas, start=1):
            print(f"{i}. Título: {nota.titulo} - Descrição: {nota.descricao}")
    else:
        print("Nenhuma nota encontrada.")

def deletar_nota(notas, indice):
    if indice < 0 or indice >= len(notas):
        print("Índice inválido.")
    else:
        del notas[indice]
        print("Nota deletada com sucesso!")

def main():
    notas = []

    while True:
        print("\nOpções:")
        print("1. Adicionar nota")
        print("2. Ver notas")
        print("3. Deletar nota")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título da nota: ")
            descricao = input("Digite a descrição da nota: ")
            adicionar_nota(notas, titulo, descricao)
        elif opcao == "2":
            exibir_notas(notas)
        elif opcao == "3":
            indice = int(input("Digite o número da nota que deseja deletar: ")) - 1
            deletar_nota(notas, indice)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()