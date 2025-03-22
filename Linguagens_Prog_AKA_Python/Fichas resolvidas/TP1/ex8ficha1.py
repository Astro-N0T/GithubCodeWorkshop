# 8. Analise, teste e comente:
a=1
b=1
print(a is b)
a=[1]
b=[1]
print(a is b)
a=[1]
b=a
print(a is b)
a=[1]
b=a+[] #ou b=a[:]
print(a is b)

#O primeiro print é true, visto que os dois objetos apontam para a mesma posição.
#O segundo print é false, poruqe apresenta duas listas diferentes
#O terceiro print é true, visto que b aponta para a, a.k.a. b=a ou a=b.
#O quarto print é false, a lista b é uma lista "sliced" da lista a, embora uma cópia exata dela continuam a ser listas dif.