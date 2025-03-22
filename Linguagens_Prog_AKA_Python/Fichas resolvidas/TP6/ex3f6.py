"""3. Dada uma lista de coordenadas (x,y):
pts = [ (2,5), (12,3), (12,1), (6,5), (14, 10), (12, 10), (8,12), (5,3) ]
Ordene as coordenadas, de acordo com os valores de y e, em caso de empate, de
acordo com os valores de x. Ambos em ordem decrescente."""
    
pts = [ (6,-1), (8,4), (7.5,-3), (4.4,12), (7,2) ]

o_maior_x = max(map(lambda p: p[0], pts))

par_maior_x = next(filter(lambda p: p[0] == o_maior_x, pts))

pts_primeiro_quadrante = list(filter(lambda p: p[0] >= 0 and p[1] >= 0, pts))

pts_para_ordenar = [ (2,5), (12,3), (12,1), (6,5), (14, 10), (12, 10), (8,12), (5,3) ]
pts_ordenados = sorted(pts_para_ordenar, key=lambda p: (-p[1], -p[0]))

print("Maior valor de x:", o_maior_x)
print("Par de coordenadas correspondente:", par_maior_x)
print("Coordenadas no primeiro quadrante:", pts_primeiro_quadrante)
print("Coordenadas ordenadas:", pts_ordenados)