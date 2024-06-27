""" Exercício 21: Conversor de Temperatura
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
garantir que a entrada seja numérica,tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
"""

try:
    graus = input("Digite temperatura em graus Celsius: ")
    graus = float(graus) #Se o usuário digitar algo que não possa ser convertido para float, um ValueError será lançado e capturado no bloco except.
    
    Fahrenheit = (graus * 1.8) + 32
    print("A temperatura {} em Fahrenheit é: {}" .format(graus,Fahrenheit))
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número.")
finally:
    # Bloco de código a ser executado sempre, independentemente de uma exceção ter ocorrido ou não
    print("Bloco finally executado.")
