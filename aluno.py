class Aluno:
    def __init__(self, matricula, nome, curso):
        # Atributos públicos básicos (sem properties)
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.notas = []  # Lista para armazenar as notas

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def determinar_situacao(self):
        if len(self.notas) == 0:
            return "Sem avaliações"
        
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        elif media >= 5.0:
            return "Recuperação"
        else:
            return "Reprovado"

    def exibir_boletim(self):
        media = self.calcular_media()
        situacao = self.determinar_situacao()
        print("\n--- BOLETIM INDIVIDUAL ---")
        print(f"Matrícula : {self.matricula}")
        print(f"Nome      : {self.nome}")
        print(f"Curso     : {self.curso}")
        print(f"Notas     : {self.notas}")
        print(f"Média     : {media:.2f}")
        print(f"Situação  : {situacao}")
        print("--------------------------")