### Exercício 13. Consumo de API Simulado
#Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

import requests
base_url = "https://api.exemplo.com/data"

params = {
    'page': 1,
    'per_page': 10  #Número de itens por página
}

#Lista para armazenar todos os itens
todos_os_itens = []

while True:
    #Faz a requisição para a API
    response = requests.get(base_url, params=params)
    
    #Verifica se a resposta é válida
    if response.status_code != 200:
        print("Erro ao fazer a requisição:", response.status_code)
        break
    
    #Converte a resposta para JSON
    data = response.json()
    
    #Adiciona os itens da página atual à lista
    todos_os_itens.extend(data['items'])
    
    #Verifica se há mais páginas
    if not data['has_more']:
        break
    
    #Incrementa o número da página para a próxima requisição
    params['page'] += 1

#Exibe o resultado final
print("Total de itens:", len(todos_os_itens))
for item in todos_os_itens:
    print(item)

    
    #Incrementa o número da página para a próxima requisição
    params['page'] += 1

#Exibe o resultado final
print("Total de itens:", len(todos_os_itens))
for item in todos_os_itens:
    print(item)
