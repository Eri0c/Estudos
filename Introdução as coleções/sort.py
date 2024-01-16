print(60*'-')

carrinho_de_compras = ["pão", "carne", "verduras", "alface"]
print(carrinho_de_compras)
#sort #ordenação
carrinho_de_compras.sort() # ordenando a lista em ordem alfabetica
print(carrinho_de_compras)
print(60*'-')

# sort() tambem ordena numeros 
lista= [1, 50, 23, 67, 100]
print(lista)

lista.sort()
print(lista)

print(60*'-')

# sort(reverse = True) para ordenar em ordem decrescente
lista= [1, 50, 23, 67, 100]
print(lista)

lista.sort(reverse = True)
# lista.reverse()  ira apenas inverter 
print(lista)

print(60*'-')

lista2 = ['Ana', 'Pedro', 'Marta', 'Clarice', 'beatriz', 'ana clara']
print(lista2)

lista2.sort(key = str.lower) # foi passado uma chave (key = str.lower ) para tratar os elementos como se todos estivessem em minusculas, 
# assim reordenou sem modificar os elementos
print(lista2)