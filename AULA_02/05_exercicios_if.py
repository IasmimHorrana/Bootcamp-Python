# If e Else
idade = 22
idade_minima = 18
idade_tirar_carteira = 18

if idade < idade_minima:
    print("Não pode dirigir.")
elif idade == idade_tirar_carteira:
    print("Pode tirar a carteira de motorista.")
else: 
    print("Pode dirigir.")

# O bloco try tenta converter as entradas do usuário para inteiros e verificar se os números são diferentes.
try:
    valor1 = input("Digite o primeiro valor: ")
    valor2 = input("Digite o segundo valor: ")

    num1 = int(valor1)
    num2 = int(valor2)

    if num1 != num2:
        print("Os números são diferentes.")
    else:
        print("Os números são iguais.")

#O bloco except ValueError captura erros de conversão se as entradas não forem números válidos.
except ValueError as e:
    print(f"Erro: Por favor, insira números válidos. Detalhes do erro: {e}")
#O bloco except TypeError está incluído para capturar possíveis erros de tipo (embora não esperados neste caso específico).
except TypeError as e:
    print(f"Erro de tipo: {e}")
