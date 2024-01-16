# Empacotar é quando adicionamos itens a lista ou tuplas. desempacotar é o inverso.

tupla = ("item1", "item2", "item3")
tupla2 = ("a", "b")

tupla3 = tupla + tupla2
print(tupla3)

print(60*'-')

"""
tupla = tupla * 3
for variavel in tupla:
    print(variavel)
"""
"""for x in tupla:
    print(x)

for x in range(len(tupla)):
    print(x,tupla[x])    
"""    
"""
outras formas de fazer a concatenação de tuplas

tupla = tupla + tupla2

tupla = tupla * 3
"""
print(tupla)
#  desempacotar é o inverso.
(x, y, z) = tupla
print("x:", x)
print("y:", y)
print("z:", z)




