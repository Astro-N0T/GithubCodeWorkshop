import json

idades = {"João": 13, "Francisco": 24}

with open("idades.json", "w", encoding="utf-8") as ficheiro:
    json.dump(idades, ficheiro, ensure_ascii=False, indent=4)

with open("idades.json", "r", encoding="utf-8") as ficheiro:
    dados_importados = json.load(ficheiro)

print(dados_importados)
