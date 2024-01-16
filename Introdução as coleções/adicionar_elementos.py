#index
lista = ["carro", "barco", "avião"]
print(lista)

print(60*'-')

lista.insert(0, "bicicleta")
print(lista)

print(60*'-')

for x in range(len(lista)):
    print(x, lista[x])


print(60*'-')

texto = "carro, avião"
lista2 = list(texto)
print(lista2)


print(60*'-')

lista.append(["moto","bicicleta","navio"])# append() recebe somente um argumento
print(lista)

lista.extend(["moto","bicicleta","navio"])


print(lista)

for x in range(len(lista)):
    print(x, lista[x])

print(60*'-')