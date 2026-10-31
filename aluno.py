class Aluno:
    def __init__(self, matricula: str, nome: str, curso: str):
        # Validação de campos vazios
        if not matricula.strip() or not nome.strip() or not curso.strip():
            raise ValueError("Os campos de matrícula, nome e curso não podem estar vazios.")
        
        self._matricula = matricula.strip()
        self._nome = nome.strip()
        self._curso = curso.strip()
        self._notas = []

    @property
    def matricula(self):
        return self._matricula

    @property
    def nome(self):
        return self._nome

    @property
    def curso(self):
        return self._curso

    @property
    def notas(self):
        return self._notas

    def adicionar_nota(self, nota: float):
        if not (0.0 <= nota <= 10.0):
            raise ValueError("A nota deve estar entre 0.0 e 10.0.")
        self._notas.append(nota)

    def calcular_media(self) -> float:
        if len(self._notas) == 0:
            return 0.0
        return sum(self._notas) / len(self._notas)

    def determinar_situacao(self) -> str:
        if len(self._notas) == 0:
            return "Sem avaliações"
        
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        elif media >= 5.0:
            return "Recuperação"
        else:
            return "Reprovado"

    def obter_boletim(self) -> str:
        media = self.calcular_media()
        situacao = self.determinar_situacao()
        notas_str = ", ".join(map(str, self._notas)) if self._notas else "Nenhuma nota registrada"
        
        return (
            f"\n--- BOLETIM INDIVIDUAL ---\n"
            f"Matrícula : {self._matricula}\n"
            f"Nome      : {self._nome}\n"
            f"Curso     : {self._curso}\n"
            f"Notas     : [{notas_str}]\n"
            f"Média     : {media:.2f}\n"
            f"Situação  : {situacao}\n"
            f"--------------------------"
        )