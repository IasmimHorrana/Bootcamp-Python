import csv

caminho_do_arquivo: str = "file.csv"

arquivo_csv: list = [] #inicializa uma lista vazia para armazenar as linhas do CSV

with open(file=caminho_do_arquivo, mode="r", encoding='utf-8') as arquivo: #abre o arquivo em modo de leitura com codificação UTF-8.
    leitor_csv = csv.DictReader(arquivo) #cria um leitor CSV que converte cada linha em um dicionário, usando os cabeçalhos da primeira linha como chaves.
    
    for linha in leitor_csv: #itera sobre as linhas do CSV, e cada linha é adicionada à lista arquivo_csv.
        arquivo_csv.append(linha)
print(arquivo_csv)

