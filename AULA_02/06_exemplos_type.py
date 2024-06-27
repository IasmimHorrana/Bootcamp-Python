# Um TypeError ocorre quando uma operação ou função é aplicada a um objeto de um tipo inadequado.
try:
    resultado = "3" + 3  # Isso causará um TypeError
except TypeError as e:
    print(f"Ocorreu um TypeError: {e}")

#Fazer uma verificação de tipo (type check) envolve verificar o tipo de um objeto para garantir que ele é do tipo esperado antes de realizar uma operação.
numero = int(input("Insira um número: "))
if isinstance(numero,int):
    print("A variavel é um inteiro.")
else:
    print("A variavel não é um inteiro.")

#A conversão de tipo (type conversion) é o processo de converter um valor de um tipo de dado para outro.
numero_str = "123"
numero_int = int(numero_str)  # Converte string para inteiro
print(numero_int)

# O bloco try-except é usado para capturar e tratar exceções que podem ocorrer durante a execução de um bloco de código.
try:
    numero = int(input("Digite um número: "))  # Pode causar ValueError se a entrada não for um número
    print(f"O número é {numero}")
except ValueError as e:
    print(f"Ocorreu um erro: {e}")







