"""Exercício 24: Classificador de Números
Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else 
para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
"""
try:
    numero = int(input("Digite um número: "))

     # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print("O número {} é par." .format(numero))
    else:
        print("O número {} é impar." .format(numero))

    if numero > 0:
        print("O número {} é positivo" .format(numero))
    elif numero < 0:
        print("O número {} é negativo" .format(numero))
    else:
        print("O número é zero.")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
