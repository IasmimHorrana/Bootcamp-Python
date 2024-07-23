#Desafio: Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, 
#filtra produtos entregues e somar os valores dos produtos. 

import csv
path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]: #Função que ler um arquivo CSV e retornar uma lista de dicionarios. 
    lista = [] 
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    lista_de_produtos_filtrado = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_de_produtos_filtrado.append(produto)
    return lista_de_produtos_filtrado

def somar_valores_dos_produtos(lista_de_produtos_filtrado: list[dict]) -> float:
    valor_total = 0.0
    for produto in lista_de_produtos_filtrado:
        valor_total += float(produto.get("price"))
    return valor_total

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(f"Valor total dos produtos entregues: R$ {valor_dos_produtos_entregues:.2f}")

