# Exercícios 
# Inteiros (int)

# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

num_01 = int(input("Digite o primeiro número: "))
num_02 = int(input("Digite o segundo número: "))
soma = num_01 + num_02
print("Total: {}" .format(soma))

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero_usuario = int(input("Digite um número: "))
resto_divisao = 5
resultado = numero_usuario % resto_divisao
print("O resto da divisão do {} por 5 é {}: " .format(numero_usuario, resultado))

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um segundo número: "))
mult = numero1 * numero2
print("A multiplicação de {} por {} é: {}" .format(numero1,numero2,mult))

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
div = numero1 // numero2
print("A divisão inteira é: {}" .format(div))

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero_usuario = int(input("Digite um número: "))
quadrado = numero_usuario * numero_usuario
print("O quadrado de {} é: {}" .format(numero_usuario, quadrado))






