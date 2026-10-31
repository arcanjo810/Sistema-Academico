# Sistema de Gestão Acadêmica (POO I)

## Objetivo
Aplicação desenvolvida em Python para simular um sistema de gestão acadêmica executado via terminal, aplicando conceitos fundamentais de Orientação a Objetos (POO), estruturas de dados, tratamento de exceções e modularização.

## Requisitos Atendidos
- **Cadastro de Alunos:** Impede matrículas duplicadas e valida campos vazios.
- **Registro de Notas:** Aceita apenas notas entre 0,0 e 10,0 com tratamento de erros de tipo.
- **Cálculo de Média e Situação:** Classifica em Aprovado (>= 7.0), Recuperação (>= 5.0 e < 7.0), Reprovado (< 5.0) ou Sem avaliações.
- **Relatórios:** Emite boletim individual e relatório estatístico geral da turma.
- **Modularização:** Organizado em `main.py`, `aluno.py` e `sistema_academico.py`.

## Como Executar
1. Certifique-se de ter o Python 3 instalado.
2. Abra a pasta do projeto no terminal ou no VS Code.
3. Execute o comando:
   ```bash
   python main.py
