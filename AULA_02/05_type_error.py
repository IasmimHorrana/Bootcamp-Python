# Exemplo TypeError

try:
    resultado = len("Iasmim")
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("Tudo ocorreu bem.")

# Isinstance é muito utilizado.

numero = int(input("Insira um número: "))
if isinstance(numero,int):
    print("A variavel é um inteiro.")
else:
    print("A variavel não é um inteiro.")

# If e Else

idade = 18
idade_minima = 18
idade_tirar_carteira = 18

if idade < idade_minima:
    print("Não pode dirigir.")
elif idade == idade_tirar_carteira:
    print("Pode tirar a carteira de motorista.")
else: 
    print("Pode dirigir.")
