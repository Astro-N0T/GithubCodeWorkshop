"""4. Crie uma função de ordem superior que aplique uma função genérica a uma lista
de items.
a) Teste com uma lista de strings e transforme em minúsculas.
b) Teste com uma lista de strings e transforme em inteiros.
c) Teste com uma lista de strings e transforme substituindo espaços por hífen.
d) Teste com uma lista de strings e transforme transformando a primeira letra
de cada palavra em Maiúsculas e o resto em minúsculas."""

pts = [ (6,-1), (8,4), (7.5,-3), (4.4,12), (7,2) ]

o_maior_x = max(map(lambda p: p[0], pts))

par_maior_x = next(filter(lambda p: p[0] == o_maior_x, pts))

pts_primeiro_quadrante = list(filter(lambda p: p[0] >= 0 and p[1] >= 0, pts))

pts_para_ordenar = [ (2,5), (12,3), (12,1), (6,5), (14, 10), (12, 10), (8,12), (5,3) ]
pts_ordenados = sorted(pts_para_ordenar, key=lambda p: (-p[1], -p[0]))

def aplica_funcao(lista, funcao):
    return list(map(funcao, lista))

lista_strings = ["Python", "PROGRAMACAO FUNCIONAL", "Teste com Strings"]
resultado_minusculas = aplica_funcao(lista_strings, lambda x: x.lower())
resultado_inteiros = aplica_funcao(["1", "2", "3"], lambda x: int(x))
resultado_hifens = aplica_funcao(lista_strings, lambda x: x.replace(" ", "-")) 

resultado_capitalize = aplica_funcao(lista_strings, lambda x: x.title())

print("Maior valor de x:", o_maior_x)
print("Par de coordenadas correspondente:", par_maior_x)
print("Coordenadas no primeiro quadrante:", pts_primeiro_quadrante)
print("Coordenadas ordenadas:", pts_ordenados)
print("Strings em minúsculas:", resultado_minusculas)
print("Strings convertidas para inteiros:", resultado_inteiros)
print("Strings com espaços substituídos por hífen:", resultado_hifens)
print("Strings com a primeira letra maiúscula:", resultado_capitalize)

