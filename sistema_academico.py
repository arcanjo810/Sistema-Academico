from aluno import Aluno

class SistemaAcademico:
    def __init__(self):
        # Dicionário onde a chave é a matrícula e o valor é o objeto Aluno
        self.alunos = {}

    def cadastrar_aluno(self, matricula, nome, curso):
        # Validação simples
        if matricula == "" or nome == "" or curso == "":
            print("Erro: Todos os campos devem ser preenchidos.")
            return False

        if matricula in self.alunos:
            print(f"Erro: Já existe um aluno cadastrado com a matrícula '{matricula}'.")
            return False

        # Criando e armazenando o objeto Aluno
        novo_aluno = Aluno(matricula, nome, curso)
        self.alunos[matricula] = novo_aluno
        print("Sucesso: Aluno cadastrado com sucesso!")
        return True

    def buscar_aluno(self, matricula):
        if matricula in self.alunos:
            return self.alunos[matricula]
        return None

    def listar_alunos(self):
        if not self.alunos:
            print("\nNenhum aluno cadastrado no sistema.")
            return

        print("\n--- LISTA DE ALUNOS CADASTRADOS ---")
        for matricula, aluno in self.alunos.items():
            print(f"Matrícula: {matricula} | Nome: {aluno.nome} | Curso: {aluno.curso}")
        print("-" * 35)

    def registrar_nota(self, matricula, nota):
        aluno = self.buscar_aluno(matricula)
        if aluno is None:
            print(f"Erro: Aluno com matrícula '{matricula}' não foi encontrado.")
            return

        if 0.0 <= nota <= 10.0:
            aluno.adicionar_nota(nota)
            print("Sucesso: Nota registrada com sucesso!")
        else:
            print("Erro: A nota deve estar entre 0.0 e 10.0.")

    def consultar_boletim(self, matricula):
        aluno = self.buscar_aluno(matricula)
        if aluno is None:
            print(f"Erro: Aluno com matrícula '{matricula}' não foi encontrado.")
            return
        
        aluno.exibir_boletim()

    def emitir_relatorio_geral(self):
        if not self.alunos:
            print("\nNenhum aluno cadastrado para emitir relatório.")
            return

        total_alunos = len(self.alunos)
        alunos_com_notas = []
        alunos_sem_notas = 0
        
        aprovados = 0
        recuperacao = 0
        reprovados = 0

        medias = []

        for aluno in self.alunos.values():
            if len(aluno.notas) > 0:
                alunos_com_notas.append(aluno)
                media = aluno.calcular_media()
                medias.append(media)
                
                situacao = aluno.determinar_situacao()
                if situacao == "Aprovado":
                    aprovados += 1
                elif situacao == "Recuperação":
                    recuperacao += 1
                elif situacao == "Reprovado":
                    reprovados += 1
            else:
                alunos_sem_notas += 1

        print("\n================ RELATÓRIO GERAL ================")
        print(f"Total de alunos cadastrados : {total_alunos}")
        print(f"Alunos com avaliações       : {len(alunos_com_notas)}")
        print(f"Alunos sem avaliações       : {alunos_sem_notas}")

        if len(medias) > 0:
            media_geral = sum(medias) / len(medias)
            maior_media = max(medias)
            menor_media = min(medias)
            print(f"Média geral da turma        : {media_geral:.2f}")
            print(f"Maior média                 : {maior_media:.2f}")
            print(f"Menor média                 : {menor_media:.2f}")
        else:
            print("Média geral da turma        : N/A (Sem notas registradas)")
            print("Maior média                 : N/A")
            print("Menor média                 : N/A")

        print("\nContagem por Situação:")
        print(f"  - Aprovados    : {aprovados}")
        print(f"  - Recuperação  : {recuperacao}")
        print(f"  - Reprovados   : {reprovados}")
        print(f"  - Sem avaliações: {alunos_sem_notas}")
        print("=================================================")