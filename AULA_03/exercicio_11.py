### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
#Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#Inicia lista para armazenar os dados de entrada
dados = []
#Loop para ler dados de entrada até que a palavra-chave "sair" seja fornecida
while True:
    entrada = input("Digite um dado (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    # Adicionar a entrada à lista de dados
    dados.append(entrada)

#Exibir os dados lidos
print("\nDados lidos:")
for dado in dados:
    print(dado)
