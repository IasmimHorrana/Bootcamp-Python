# Exercicios
# Booleanos (bool)

# 1 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

# 2 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

valor1 = input("Digite o primeiro valor booleano (True/False): ")
valor2 = input("Digite o segundo valor booleano (True/False): ")
# Converte as entradas de texto em valores booleanos
valor1 = valor1 == "True"
valor2 = valor2 == "True"
resultado = valor1 or valor2
print("Resultado da operação OR:", resultado)

# 3 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor = input("Digite um valor booleano (True/False): ")
valor_booleano = valor == "True"
valor_invertido = not valor_booleano
print("Valor invertido:", valor_invertido)

# 4 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
sao_iguais = numero1 == numero2
print("Os números são iguais:", sao_iguais)

# 5 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
sao_diferentes = numero1 != numero2
print("Os números são diferentes:", sao_diferentes)
