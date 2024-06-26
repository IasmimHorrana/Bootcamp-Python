# Desafio - Cálculo de Bônus com Entrada do Usuário

bonus_anual = 1000
usuario = input("Digite o seu nome: ")
salario_mensal = float(input("Digite o valor do seu salario mensal: "))
bonus_mensal = float(input("Digite o valor do bonus mensal: "))
valor_bonus = bonus_anual + salario_mensal * bonus_mensal

print("Olá {}, seu bônus foi de: {}".format(usuario, valor_bonus))



