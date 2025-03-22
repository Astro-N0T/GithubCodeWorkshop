"""2. Dada a mesma lista de coodenadas (x,y):
pts = [ (6,-1), (8,4), (7.5,-3), (4.4,12), (7,2) ]
a) Filtre a lista anterior, de forma a remover as coordenadas com componentes
negativas. Só queremos o primeiro quadrante."""

pts = [ (6,-1), (8,4), (7.5,-3), (4.4,12), (7,2) ]

o_maior_x = max(map(lambda p: p[0], pts))

par_maior_x = next(filter(lambda p: p[0] == o_maior_x, pts))

pts_primeiro_quadrante = list(filter(lambda p: p[0] >= 0 and p[1] >= 0, pts))

print("Maior valor de x:", o_maior_x)
print("Par de coordenadas correspondente:", par_maior_x)
print("Coordenadas no primeiro quadrante:", pts_primeiro_quadrante)