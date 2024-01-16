# Devemos utilizar a tupla quando queremos criar uma lista que nao queremos que seja modificada

lista = ["item1", "item2", "item3"] # lista é mutavél
print(lista)
print(len(lista))
print(type(lista))

print(60*'-')


# index   0         1        2         3        4
tupla = ("item1", "item2", "item3", "item1", "item1") # Tupla é imutavel
print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[2])

print(tupla.count("item1")) # contando quantas vezes tem "item1"