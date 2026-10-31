from aluno import Aluno

class SistemaAcademico:
    def __init__(self):
        # Utilização de dicionário para garantir busca eficiente por matrícula (chave única)
        self._alunos = {}

    def cadastrar_aluno(self, matricula: str, nome: str, curso: str):
        matricula_limpa = matricula.strip()
        if matricula_limpa in self._alunos:
            raise ValueError(f"Erro: Já existe um aluno cadastrado com a matrícula '{matricula_limpa}'.")
        
        novo_aluno = Aluno(matricula_limpa, nome, curso)
        self._alunos[matricula_limpa] = novo_aluno
        return novo_aluno

    def buscar_aluno(self, matricula: str) -> Aluno:
        matricula_limpa = matricula.strip()
        if matricula_limpa not in self._alunos:
            raise KeyError(f"Erro: Aluno com a matrícula '{matricula_limpa}' não foi encontrado.")
        return self._alunos[matricula_limpa]

    def listar_alunos(self):
        if not self._alunos:
            print("\nNenhum aluno cadastrado no sistema.")
            return
        
        print("\n--- LISTA DE ALUNOS CADASTRADOS ---")
        for aluno in self._alunos.values():
            print(f"Matrícula: {aluno.matricula} | Nome: {aluno.nome} | Curso: {aluno.curso} | Notas: {len(aluno.notas)}")
        print("-" * 40)

    def registrar_nota(self, matricula: str, nota: float):
        aluno = self.buscar_aluno(matricula)
        aluno.adicionar_nota(nota)

    def consultar_boletim(self, matricula: str):
        aluno = self.buscar_aluno(matricula)
        print(aluno.obter_boletim())

    def emitir_relatorio_geral(self):
        if not self._alunos:
            print("\nNenhum aluno cadastrado para emitir relatório.")
            return

        total_alunos = len(self._alunos)
        alunos_com_notas = [a for a in self._alunos.values() if len(a.notas) > 0]
        alunos_sem_notas = total_alunos - len(alunos_com_notas)

        contagem_situacao = {
            "Aprovado": 0,
            "Recuperação": 0,
            "Reprovado": 0,
            "Sem avaliações": alunos_sem_notas
        }

        medias = []
        for aluno in alunos_com_notas:
            media = aluno.calcular_media()
            medias.append(media)
            situacao = aluno.determinar_situacao()
            contagem_situacao[situacao] += 1

        print("\n================ RELATÓRIO GERAL DO SISTEMA ================")
        print(f"Total de alunos cadastrados : {total_alunos}")
        print(f"Alunos com avaliações       : {len(alunos_com_notas)}")
        print(f"Alunos sem avaliações       : {alunos_sem_notas}")

        if medias:
            media_geral = sum(medias) / len(medias)
            maior_media = max(medias)
            menor_media = min(medias)
            print(f"Média geral da turma        : {media_geral:.2f}")
            print(f"Maior média                 : {maior_media:.2f}")
            print(f"Menor média                 : {menor_media:.2f}")
        else:
            print("Média geral da turma        : N/A (Nenhum aluno possui notas registradas)")
            print("Maior média                 : N/A")
            print("Menor média                 : N/A")

        print("\nContagem por Situação:")
        for sit, qtd in contagem_situacao.items():
            print(f"  - {sit}: {qtd}")
        
        print("\nNota sobre empates:")
        print("  Em caso de empate na maior ou menor média, o sistema considera o valor numérico idêntico.")
        print("  O cálculo geral ignora alunos sem notas para evitar distorções estatísticas.")
        print("============================================================")