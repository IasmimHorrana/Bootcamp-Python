""" Exercício 4: Validação de Dados de Entrada

# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido 
um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.
"""

import re  # Importa o módulo de expressões regulares

# Validação da idade
while True:
    entrada_idade = input("Digite sua idade: ")
    try:
        idade = int(entrada_idade)
        if not 18 <= idade <= 65:
            print("Idade fora do intervalo permitido (18-65 anos).")
        else:
            print(f"Você digitou uma idade válida: {idade}")
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Validação do e-mail
while True:
    entrada_email = input("Digite um e-mail: ")
    # Utiliza re.match() para verificar se a entrada corresponde ao padrão de um e-mail válido
    if re.match(r"[^@]+@[^@]+\.[^@]+", entrada_email):
        print(f"Você digitou um e-mail válido: {entrada_email}")
        break
    else:
        print("Entrada inválida. Por favor, digite um e-mail válido.")

