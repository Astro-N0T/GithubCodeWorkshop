# 3. O Utilizando os geradores (como nas List Comprehension), crie uma função que
# leia de um ficheiro linha a linha e uma outra função que escreva noutro, mas
# filtrando os ‘#. Nota: o método writelines aceita iteráveis

def ler_ficheiro_como_gerador(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
            for linha in ficheiro:
                if not linha.strip().startswith('#'):
                    yield linha
    except FileNotFoundError:
        return

def escrever_ficheiro_de_gerador(gerador, nome_ficheiro_saida):
    with open(nome_ficheiro_saida, 'w', encoding='utf-8') as ficheiro:
        ficheiro.writelines(gerador)
