""" Exercício 22: Verificador de Palíndromo
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
"""

try:
    palavra = input("Digite uma palavra: ")
    
    if not isinstance(palavra, str): #Verificar se a entrada é uma string
        raise ValueError("Entrada inválida. Por favor, digite uma string.")
    # Remover espaços e pontuações da entrada
    palavra_tratada = palavra.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("-", "").replace(":", "").replace(";", "")
    # Verificar se a palavra tratada é um palíndromo
    if palavra_tratada == palavra_tratada[::-1]:
        print(f'A entrada "{palavra}" é um palíndromo!')
    else:
        print(f'A entrada "{palavra}" não é um palíndromo.')

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite uma palavra.")
finally:
    print("Bloco finally executado.")


