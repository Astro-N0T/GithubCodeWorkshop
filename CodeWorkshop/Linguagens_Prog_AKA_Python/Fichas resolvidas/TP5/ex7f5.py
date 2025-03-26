# 7.Desenvolva uma função geradora ou expressão geradora onde que dada uma
#entrada iterável, devolve (filtra) os valores que são ímpares.

def filtrar_impares(iteravel):
    for valor in iteravel:
        if valor % 2 != 0:
            yield valor

entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = (valor for valor in entrada if valor % 2 != 0)
print(list(resultado))