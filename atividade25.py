
# Inicializa o contador de alunos aprovados
aprovados = 0

# Loop para receber a nota de 5 alunos
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    
    # Verifica se a nota é maior ou igual a 7
    if nota >= 7:
        aprovados += 1

# Exibe o número de alunos aprovados
print(f"Número de alunos aprovados: {aprovados}")