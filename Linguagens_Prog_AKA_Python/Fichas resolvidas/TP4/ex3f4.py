# ao pegar no codigo do ex1 e ex2
indice= ("1\n2\n3\n4\n5\n\n66\n77\n88\n99\ncem")

with open('ex3f4.txt', 'w') as file:
    file.write(indice)

with open('ex3f4.txt', 'r') as file:
    read=file.read()
    
print(read)

