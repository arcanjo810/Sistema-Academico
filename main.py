from sistema_academico import SistemaAcademico

def exibir_menu():
    print("\n================ SISTEMA ACADÊMICO ================")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Buscar Aluno por Matrícula")
    print("4. Registrar Nota")
    print("5. Consultar Boletim")
    print("6. Emitir Relatório Geral")
    print("7. Sair")
    print("====================================================")

def main():
    sistema = SistemaAcademico()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-7): ").strip()

        if opcao == "1":
            print("\n--- CADASTRO DE ALUNO ---")
            matricula = input("Digite a matrícula: ")
            nome = input("Digite o nome completo: ")
            curso = input("Digite o curso: ")
            try:
                sistema.cadastrar_aluno(matricula, nome, curso)
                print("Sucesso: Cadastro confirmado.")
            except ValueError as e:
                print(f"{e}")

        elif opcao == "2":
            sistema.listar_alunos()

        elif opcao == "3":
            print("\n--- BUSCA DE ALUNO ---")
            matricula = input("Digite a matrícula do aluno: ")
            try:
                aluno = sistema.buscar_aluno(matricula)
                print(f"\n[Aluno Encontrado]\nMatrícula: {aluno.matricula}\nNome: {aluno.nome}\nCurso: {aluno.curso}")
            except (ValueError, KeyError) as e:
                print(f"{e}")

        elif opcao == "4":
            print("\n--- REGISTRAR NOTA ---")
            matricula = input("Digite a matrícula do aluno: ")
            try:
                nota_str = input("Digite a nota (0 a 10): ")
                nota = float(nota_str)
                sistema.registrar_nota(matricula, nota)
                print("Sucesso: Nota registrada com sucesso.")
            except ValueError as e:
                if "could not convert string to float" in str(e):
                    print("Erro: Entrada inválida. Digite um número válido para a nota.")
                else:
                    print(f"{e}")
            except KeyError as e:
                print(f"{e}")

        elif opcao == "5":
            print("\n--- CONSULTAR BOLETIM ---")
            matricula = input("Digite a matrícula do aluno: ")
            try:
                sistema.consultar_boletim(matricula)
            except (ValueError, KeyError) as e:
                print(f"{e}")

        elif opcao == "6":
            sistema.emitir_relatorio_geral()

        elif opcao == "7":
            print("\nEncerrando o Sistema Acadêmico. Até logo!")
            break
        else:
            print("\nErro: Opção inválida. Escolha um número entre 1 e 7.")

if __name__ == "__main__":
    main()