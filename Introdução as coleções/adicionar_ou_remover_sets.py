set1 = {"item1", "item2", "item3"}
print(set1)
set1.add("item5")
print(set1)
set1.add(8)
set1.add(True)
print(set1)


print(30*'-','x',30*'-')

# Função update adicionando elementos ao meu set
set1 = {4, 5, 7, 8, 9, 1}
#set2 = {"item3", "item5", "item1"}
set1.update([1, 4, 7, 8, 9, 3, "item5","item6"])

print(set1)


print(30*'-','x',30*'-')

# removendo elementos do meu set (sempre sera removido de modo aleatorio)
set1 = {1, 3, 4, 5, 7, 8, 9, 'item5', 'item6'}
print(set1)
set1.pop()

print(set1)
set1.remove("item5")# se eu for remover um item que nao existe sera apresentado um erro
print(f'Removendo um item selecionado: no caso o item5 {set1}')

set1.discard("item6")# difereça para remove > neste caso nao sera apresentado erro
print(f"Removendo um item selecionado: no caso o item6 {set1}")

"""del set1
print(set1) # sera apresentado erro
"""

set1.clear()# exclui todos os elementos do  meu set, retornando um set vazio
print(set1)

