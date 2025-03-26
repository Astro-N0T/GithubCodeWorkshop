# 2. Repita o ponto anterior, mas filtrando (removendo) as linhas que começam por
# com ‘#’.


def ler_ficheiro_filtrado(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
            return [linha.strip() for linha in ficheiro if not linha.strip().startswith('#')]
    except FileNotFoundError:
        return 0
