"""1. Dada uma lista de coordenadas (x,y):
pts = [ (6,-1), (8,4), (7.5,-3), (4.4,12), (7,2) ]
a) Analise e recolha o maior valor de x, de todos os pontos.
b) Recolha o par de coordenadas, referente à alínea anterior."""

pts = [ (6,-1), (8,4), (7.5,-3), (4.4,12), (7,2) ]

o_maior_x = max(map(lambda p: p[0], pts))

par_maior_x = next(filter(lambda p: p[0] == o_maior_x, pts))

print("Maior valor de x:", o_maior_x)
print("Par de coordenadas correspondente:", par_maior_x)