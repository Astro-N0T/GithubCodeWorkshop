import json

lista_dicionarios = [{"João": 13}, {"Francisco": 24}, {"Ana": 19}]

with open("lista_idades.json", "w", encoding="utf-8") as ficheiro:
    json.dump(lista_dicionarios, ficheiro, ensure_ascii=False, indent=4)

with open("lista_idades.json", "r", encoding="utf-8") as ficheiro:
    dados_importados = json.load(ficheiro)

print(dados_importados)
