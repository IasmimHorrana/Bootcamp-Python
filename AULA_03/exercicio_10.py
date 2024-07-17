### Exercício 10. Agregação de Dados por Categoria
#Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {'id': 1, 'produto': 'Notebook', 'categoria': 'Eletrônicos', 'quantidade': 2, 'preço': 3500.00, 'data': '2023-07-01'},
    {'id': 2, 'produto': 'Teclado', 'categoria': 'Periféricos', 'quantidade': 5, 'preço': 150.00, 'data': '2023-07-02'},
    {'id': 3, 'produto': 'Mouse', 'categoria': 'Periféricos', 'quantidade': 10, 'preço': 80.00, 'data': '2023-07-03'},
    {'id': 4, 'produto': 'Monitor', 'categoria': 'Eletrônicos', 'quantidade': 3, 'preço': 1200.00, 'data': '2023-07-04'},
    {'id': 5, 'produto': 'Notebook', 'categoria': 'Eletrônicos', 'quantidade': 1, 'preço': 3500.00, 'data': '2023-07-05'},
]

categoria_especifica = 'Eletrônicos'

valor_total_eletronicos = sum(venda['quantidade'] * venda['preço'] for venda in vendas if venda['categoria'] == categoria_especifica)

print(f"Valor total das vendas de {categoria_especifica}: R${valor_total_eletronicos:.2f}")
