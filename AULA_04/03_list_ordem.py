lista_de_numero = [40,2,35,0,-460,1,9]

def ordenar_lista(numeros: list) -> list:
    nova_lista = numeros.copy()

    for i in range(len(nova_lista)):
        for j in range(i+1, len(nova_lista)):
            if nova_lista[i] > nova_lista[j]:
                nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]
    return nova_lista

nova_lista_num = ordenar_lista(lista_de_numero)
print(nova_lista_num)

#Segue uma forma de puxar essa função a cima em um outro arquivo se houvesse necessidade:
#from 03_list_ordem import ordenar_lista
#lista_de_numero = [40, 2, 35, 0, -460, 1, 9]
#nova_lista_num = ordenar_lista(lista_de_numero) #Usar a função importar do módulo
#print(nova_lista_num)
