### Exercício 8. Filtragem de Dados Faltantes
#Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# Lista de dicionários representando dados de usuários
usuarios = [
    {'nome': 'Ruka', 'idade': 22, 'email': 'ruka@example.com'},
    {'nome': 'Rami', 'idade': 17},
    {'nome': 'Asa', 'idade': 19, 'email': 'asa@example.com'},
    {'nome': 'Canny', 'email': 'canny@example.com'},
]

# Filtrar dicionários que possuem o campo 'email'
usuarios_com_email = [usuario for usuario in usuarios if 'email' in usuario]

# Exibir a lista filtrada
print("Usuários com email:")
for usuario in usuarios_com_email:
    print(usuario)

