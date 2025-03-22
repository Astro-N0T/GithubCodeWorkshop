"""6. Crie uma 2 funções que, dada uma lista de strings:
a) Expanda a lista e crie uma lista de palavras (separador é o espaço):
b) Remova (filtre) as palavras com menos de 4 letras"""

pts = [ (6,-1), (8,4), (7.5,-3), (4.4,12), (7,2) ]

o_maior_x = max(map(lambda p: p[0], pts))

par_maior_x = next(filter(lambda p: p[0] == o_maior_x, pts))

pts_primeiro_quadrante = list(filter(lambda p: p[0] >= 0 and p[1] >= 0, pts))

pts_para_ordenar = [ (2,5), (12,3), (12,1), (6,5), (14, 10), (12, 10), (8,12), (5,3) ]
pts_ordenados = sorted(pts_para_ordenar, key=lambda p: (-p[1], -p[0]))

def aplica_funcao(lista, funcao):
    return list(map(funcao, lista))

def toCamelCase(lista):
    return aplica_funcao(lista, lambda x: ''.join(word.capitalize() for word in x.split()))

def expande_palavras(lista):
    return [palavra for frase in lista for palavra in frase.split()]

def filtra_palavras(lista):
    return list(filter(lambda palavra: len(palavra) >= 4, lista))

lista_strings = ["Python", "PROGRAMACAO FUNCIONAL", "Teste com Strings"]
resultado_minusculas = aplica_funcao(lista_strings, lambda x: x.lower())
resultado_inteiros = aplica_funcao(["1", "2", "3"], lambda x: int(x))
resultado_hifens = aplica_funcao(lista_strings, lambda x: x.replace(" ", "-"))
resultado_capitalize = aplica_funcao(lista_strings, lambda x: x.title())
resultado_camel_case = toCamelCase(lista_strings)
resultado_expande = expande_palavras(lista_strings)
resultado_filtra = filtra_palavras(resultado_expande)

print("Maior valor de x:", o_maior_x)
print("Par de coordenadas correspondente:", par_maior_x)
print("Coordenadas no primeiro quadrante:", pts_primeiro_quadrante)
print("Coordenadas ordenadas:", pts_ordenados)
print("Strings em minúsculas:", resultado_minusculas)
print("Strings convertidas para inteiros:", resultado_inteiros)
print("Strings com espaços substituídos por hífen:", resultado_hifens)
print("Strings com a primeira letra maiúscula:", resultado_capitalize)
print("Strings em CamelCase:", resultado_camel_case)
print("Lista expandida em palavras:", resultado_expande)
print("Lista filtrada (palavras com 4 ou mais letras):", resultado_filtra)
