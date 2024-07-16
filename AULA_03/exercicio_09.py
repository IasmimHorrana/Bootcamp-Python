### Exercício 9. Extração de Subconjuntos de Dados
#Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = [1,2,3,4,5,6,7,8,9,10]

num_pares = [numero for numero in numeros if numero % 2 == 0]

print("Números pares da lista: ")
print(num_pares)