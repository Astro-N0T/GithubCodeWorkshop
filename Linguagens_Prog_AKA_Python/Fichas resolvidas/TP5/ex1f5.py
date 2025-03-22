#1. Utilizando List Comprehension, crie uma função leia o conteúdo de um ficheiro
# para uma lista (linha a linha).

def ler_ficheiro_para_lista(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
            return [linha.strip() for linha in ficheiro]
    except FileNotFoundError:
        return 0
