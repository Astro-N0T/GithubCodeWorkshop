# Na função de leitura imprima o dobro do valor em cada linha. 
# Se a linha estiver em branco ou não for um número deve imprimir 0


with open('ex3f4.txt', 'r') as file:
    for linha in file:
            linha = linha.strip()
            try:
                numero = int(linha)
                print(numero * 2)
            except ValueError:
                print("0")
            
