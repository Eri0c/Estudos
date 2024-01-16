lista = ["Chicago", "Queens", "Salvador", "Pernambuco"]
print(lista)

print(60*'-')

lista2 = [2, 3 , 7, 8, 10]
print(lista2)

print(60*'-')

lista3= [2.0, 3.5, 6.3]
print(lista3)

print(60*'-')

lista4 = [True, False]
print(lista4)

print(60*'-')

# index    0        1       2     3    4
lista5 = [True, "Chicago", 2.5, False, 4]
print(lista5)
print(lista5[::])  # Exibe o mesmo que print(lista5), ou seja, todos os elementos da lista, ou começo e fim
print(lista5[1:]) # elemento  posição 1
print(lista5[2:]) # posição 2
print(lista5[-1]) # Faz um giro e mosta o ultimo elemento(começa do fim para o inicio)
print(lista5[:3]) # retorna do começo da lista até o index -1
print(lista5[:4]) # retorna do começo da lista até o index -1
print(lista5[1:4]) #retorna do index destacado até o index -1 
print(lista5[1:5:1])

print(60*'-')     


# Verificando o tipo (list)
print(type(lista))

print(60*'-')

print(lista5[1])


