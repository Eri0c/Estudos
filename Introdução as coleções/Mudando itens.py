lista = ["Gato", "Cachorro", "Peixe", "Cavalo", "Tubarão", "Girafa"]
print(lista)

print(60*'-')

print(type(lista))
print(lista[1])


print(60*'-')

# Modificando o item da lista
lista[1] = "Cavalo" 
print(lista)

print(60*'-')

# Modificando os itens da lista
lista[1:4] = ["Águia", "Morcego ", "Elefante",]
print(lista)


print(60*'-')

lista[1:2] = ["Águia", "Elefante"]
print(lista)


print(60*'-')
lista[1:5] = ["Tubarão"] # Modificou os elementos 1, 2, 3 por Tubarão sem repetir
print(lista)
print(len(lista))



print(60*'-')