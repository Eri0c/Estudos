#  Uma tupla é definida pela separação por virgula.
tupla = "item1", "item2", "item3", "item4"

print(tupla)
print(type(tupla))

print(60*'-')

# para alterar a tupla transformamaos ela em lista.
lista = list(tupla)
print(lista)
print(type(lista))

lista.append("item5") # Adicionando um item a lista.
print(lista)

print(60*'-')

tupla = tuple(lista) # recriando a minha tupla depoois de modificada
print(tupla)




