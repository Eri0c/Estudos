"""
listas: coleção ordenada, mutável e que permite valores duplicados
tuplas: coleção ordenada, imutável e que permite valores duplicados
dicionarios : coleção nao ordenada, mutável e que nao permite valores duplicados.
sets : coleção nao ordenada, imutável e que nao permite valores duplicados"""

# os Sets também são conhecidos como conjuntos.

conjunto = {"item1", "item2", "item3","item3", "item1", "item2", 3, True, 4.7, "são paulo"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))

print(30*'-','x',30*'-')

# Transformando tupla em set
tupla = (3, 7, 9, 5)
conjunto = set(tupla)
#conjunto = set((3, 7, 9, 5))  mesmo resultado
print(conjunto)
print(type(conjunto))

print(30*'-','x',30*'-')


# acessar os itens  do meu set atraves do laço de repetição for
conj = {"item1", "item2", "item3", "item4", "item5"}

for x in conj:
    print(x)

    
print(30*'-','x',30*'-')

# acressar os itens do meu set atraves do operador de associação in
conjunto = {"item", 4, 6, 8, 9, 1}
print(11 in conjunto)
