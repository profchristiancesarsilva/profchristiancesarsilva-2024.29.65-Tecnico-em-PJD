# Primeiramente, vamos pedir ao usuário para informar o número de alunos
num_alunos = int(input("Digite o número de alunos: "))  # Pergunta quantos alunos

# Criamos duas listas vazias para armazenar os alunos aprovados e reprovados
aprovados = []  # Lista de alunos que foram aprovados
reprovados = []  # Lista de alunos que foram reprovados

# Agora, vamos processar cada aluno
for i in range(num_alunos):
    print(f"\nAluno {i + 1}:")  # Mostra qual aluno estamos processando

    # Pedimos o nome do aluno
    nome = input("Digite o nome do aluno: ")

    # Criamos uma lista vazia para armazenar as notas do aluno
    notas = []  # Lista de notas do aluno

    # Vamos coletar 3 notas para cada aluno
    for j in range(3):  # Vamos pedir 3 notas
        nota = float(input(f"Digite a {j + 1}ª nota do aluno: "))  # Solicita a nota
        notas.append(nota)  # Adiciona a nota na lista de notas

    # Agora, calculamos a média do aluno
    media = sum(notas) / len(notas)  # A média é a soma das notas dividida pelo número de notas

    # Agora, vamos verificar se o aluno foi aprovado, está de recuperação ou reprovado
    if media >= 7:  # Se a média for maior ou igual a 7, o aluno foi aprovado
        situacao = "Aprovado"
        aprovados.append((nome, media))  # Adiciona o aluno à lista de aprovados
    elif media >= 5:  # Se a média for entre 5 e 7, o aluno está de recuperação
        situacao = "Recuperação"
        reprovados.append((nome, media))  # Adiciona o aluno à lista de reprovados
    else:  # Se a média for menor que 5, o aluno foi reprovado
        situacao = "Reprovado"
        reprovados.append((nome, media))  # Adiciona o aluno à lista de reprovados

    # Exibe o boletim do aluno
    print(f"\nBoletim do aluno {nome}:")
    print(f"Média: {media:.2f}")  # Exibe a média com 2 casas decimais
    print(f"Situação: {situacao}")  # Exibe a situação do aluno

# Após processar todos os alunos, vamos exibir a listagem dos alunos aprovados
print("\n--- Alunos Aprovados ---")
for aluno in aprovados:  # Para cada aluno na lista de aprovados
    print(f"Nome: {aluno[0]}, Média: {aluno[1]:.2f}")  # Exibe nome e média do aluno aprovado

# Exibe a listagem dos alunos reprovados ou de recuperação
print("\n--- Alunos Reprovados ou em Recuperação ---")
for aluno in reprovados:  # Para cada aluno na lista de reprovados ou recuperação
    print(f"Nome: {aluno[0]}, Média: {aluno[1]:.2f}")  # Exibe nome e média do aluno reprovado
