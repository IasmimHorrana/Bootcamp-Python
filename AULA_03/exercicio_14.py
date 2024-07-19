### Exercício 14. Tentativas de Conexão
#Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_max = 3
tentativa = 1

while tentativa <= tentativas_max:
    print(f"Tentativa {tentativa} de {tentativas_max}")
    #Simulação de uma tentativa de conexão
    #Aqui iria o código para tentar conectar
    if True:  #Suponha que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")