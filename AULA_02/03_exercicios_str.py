# Exercícios 
# Strings (str)

# 1 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

usuario = input("Digite uma string: ")
conversao = usuario.upper()
print(conversao)

# 2 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

usuario = input("Digite seu nome completo: ")
conversao = usuario.lower()
print(conversao)

# 3 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase_usuario = input("Digite uma frase: ")
conversao = frase_usuario.strip()
print(conversao)

# 4 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_user = input("Digite uma data de nascimento no formato dd/mm/aaaa: ")
dia, mes, ano = data_user.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# 5 - Escreva um programa que concatene duas strings fornecidas pelo usuário.

text1 = input("Digite a primeira parte do texto: ")
text2 = input("Digite a segunda parte do texto: ")
texto_concatenado = text1 + text2
print("Texto concatenado:", texto_concatenado)

