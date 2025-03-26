# Implemente uma função que imprima no ecrã apenas as linhas ímpares.

with open('ex3f4.txt', 'r') as file:
    for idx,linha in enumerate(file):
        if idx % 2 != 0 :
            print(linha.strip())
    read=file.read()
            
print(read)