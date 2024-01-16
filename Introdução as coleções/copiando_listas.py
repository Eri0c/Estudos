# 3 forma de juntar listas
"""
lista = ["a", "b", "c"]
lista2 = [1, 4, 6]

#lista = lista + lista2 # aqui somente estou concatenando as listas
#print(lista)

print(60*'-')

#lista.extend(lista2)
#print(lista)

print(60*'-')

for x in lista2:
    lista.append(x)
print(lista)    

print(60*'-')

"""

lista = ["a", "b", "c"]
print(f'lista: {lista}')

print(60*'-')

lista2 = lista.copy()

print(f'lista2:{lista2}')

print(60*'-')

lista2.append('d') # desta forma foi adcionado a letra 'd', porem ela foi adicionada nas duas listas
lista.append('e') # desta forma foi adcionado a letra 'e', porem ela foi adicionada nas duas listas

print(f'lista: {lista}')

print(60*'-')

print(f'lista2:{lista2}')

print(60*'-')

