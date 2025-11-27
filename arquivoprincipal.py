Bd = {}

def cadastrar_aluno():
    print("\n=== Cadastro ===")
    while True:
        try:
            matricula = int(input("Matrícula: "))
            break
        except ValueError:
            print("Digite um número válido.")

    if matricula in Bd:
        print("Essa matrícula já existe.")
        return

    nome = input("Nome: ")

    while True:
        try:
            nota = float(input("Nota: "))
            if 0 <= nota <= 10:
                break
            else:
                print("A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")

    Bd[matricula] = {"nome": nome, "nota": nota}
    print("Aluno cadastrado!")

def atualizar_aluno():
    print("\n=== Atualizar ===")
    try:
        matricula = int(input("Matrícula: "))
    except ValueError:
        print("Inválido.")
        return

    if matricula not in Bd:
        print("Aluno não encontrado.")
        return

    aluno = Bd[matricula]

    novo_nome = input(f"Nome atual ({aluno['nome']}): ")
    if novo_nome.strip() != "":
        aluno["nome"] = novo_nome

    nova_nota = input(f"Nota atual ({aluno['nota']}): ")
    if nova_nota.strip() != "":
        try:
            nova_nota = float(nova_nota)
            if 0 <= nova_nota <= 10:
                aluno["nota"] = nova_nota
            else:
                print("Nota fora do intervalo. Mantida.")
        except ValueError:
            print("Valor inválido. Mantida.")

    print("Atualizado.")

def deletar_aluno():
    print("\n=== Deletar ===")
    try:
        matricula = int(input("Matrícula: "))
    except ValueError:
        print("Inválido.")
        return

    if matricula in Bd:
        del Bd[matricula]
        print("Deletado.")
    else:
        print("Aluno não encontrado.")

def listar_alunos():
    print("\n=== Lista ===")
    if not Bd:
        print("Nenhum aluno.")
        return

    for mat, dados in Bd.items():
        print(f"{mat} | {dados['nome']} | {dados['nota']}")

def buscar_aluno():
    print("\n=== Buscar ===")
    try:
        matricula = int(input("Matrícula: "))
    except ValueError:
        print("Inválido.")
        return

    if matricula in Bd:
        dados = Bd[matricula]
        print(f"{dados['nome']} | Nota: {dados['nota']}")
    else:
        print("Não encontrado.")

def menu():
    while True:
        print("\n1-Cadastrar\n2-Atualizar\n3-Deletar\n4-Listar\n5-Buscar\n6-Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            atualizar_aluno()
        elif opcao == "3":
            deletar_aluno()
        elif opcao == "4":
            listar_alunos()
        elif opcao == "5":
            buscar_aluno()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Inválida.")

menu()
