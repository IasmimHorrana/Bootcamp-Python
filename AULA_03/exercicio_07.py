""" Exercício 7 - Normalização de Dados
Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
"""

numeros = [10, 20, 30, 40, 50]

min_valor = min(numeros)
max_valor = max(numeros)

numeros_normalizados = [] #Lista onde os valores normalizados serão guardados

for numero in numeros: #Normalizar cada número na lista para a escala 0 a 1
    valor_normalizado = (numero - min_valor) / (max_valor - min_valor)
    numeros_normalizados.append(valor_normalizado)

print("Lista Original:", numeros)
print("Lista Normalizada (0 a 1):", numeros_normalizados)