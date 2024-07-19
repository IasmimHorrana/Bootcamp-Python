### Exercício 15. Processamento de Dados com Condição de Parada
#Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, 4, 5, 6, 999, 7, 8, 9]

valor_parada = 999

#Inicializar o índice
i = 0

#Processar itens até encontrar o valor de parada
while i < len(itens) and itens[i] != valor_parada:
    #Processar o item
    print(itens[i])
    #Incrementar o índice
    i += 1

print("Processamento parado. Valor de parada encontrado.")
