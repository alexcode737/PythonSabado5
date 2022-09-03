tupla = (1,2,3,4,5)

print(tupla)

for numero in tupla:
    print(numero)

# tupla.append(100)
# print(tupla)

#Transformando una tupla en una lista
tuplaALista = list(tupla)
print(tuplaALista)

listaATupla = tuple(tuplaALista)
print(listaATupla)