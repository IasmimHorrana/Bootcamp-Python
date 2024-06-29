"""
Exercício 2: Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa 
classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. 
"""
try:
    temperatura = float(input("Digite a temperatura: "))

    if temperatura < 15:
        print("Temperatura baixa.")
    elif 15 <= temperatura <= 25:
        print("Temperatura normal.")
    elif temperatura > 25:
        print("Temperatura alta.")
    else:
        print("Dados inválidos")

except ValueError:
    print("Erro: Por favor, insira números válidos.")  
    