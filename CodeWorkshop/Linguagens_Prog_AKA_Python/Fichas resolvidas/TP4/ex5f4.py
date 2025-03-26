# deve abrir um error visto que nao tenho nenhum poo.txt, "file not found"

#note to self, ele tenta ler no with portanto o with tem de ficar dentro do try.
try:
    with open('poo.txt', 'r') as file:
        file.read()
except FileNotFoundError:
    print("File does not exist")


