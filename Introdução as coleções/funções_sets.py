# utilizando funções principar do sets

conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

print(30*'-', 'x', 30*'-')

# intersecção
conjunto4 = conjunto1.intersection(conjunto2)
conjunto1.intersection_update(conjunto2)# ira substituir o conjunto 1 pela intersecção do conjunto 1 com o conjunto 2
print(conjunto4)

print(30*'-', 'x', 30*'-')
# pedindo os itens que estão presentes no conjunto 1 mas que nao estao no conjunto 2
conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

print(30*'-', 'x', 30*'-')

conjunto4= conjunto1.difference(conjunto2)
#conjunto1.difference_update(conjunto2) Substituindo o conjunto 1 pela diferença dos conjuntos
print(conjunto4)

print(30*'-', 'x', 30*'-')

# pedindo os elementos que nao estao presentes em ambos conjuntos. 
conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

conjunto4= conjunto1.symmetric_difference(conjunto2)
#conjunto1.symmetric_difference_update(conjunto2) substituindo o conjunto 1 pela diferença entre os conjuntos
print(conjunto4)
