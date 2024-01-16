dicio = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}

print(dicio)

print(60*'-')

dicio["nome"] = "Pedro" # Modificando valores do dicionario
print(dicio)

print(60*'-')

dicio.update({"nome": "Ana"})# modificanto os valores do dicionario usando função update()
print(dicio)

print(60*'-')

dicio.update({"idade": 32}) # Adicionando uma chave no dicionario usando função update()
print(dicio)

print(60*'-')

dicio.update({"estado": "Rio de Janeiro"}) # Adicionando uma chave no dicionario usando função update()
print(dicio)


print(60*'-')

dados = {"nome": "Grabriel", "ano": 1993, "valor_logico": True}
dados.update ({"estado": "Rio de Janeiro"})
print(f'Dicionario dados:{dados}')

print(30*'-','x',30*'-')

dados.popitem()
print(dados) # Excluindo o ultimo elemento(chave), com a função popitem()

print(60*'-')

dados.pop("valor_logico")# eliminando um valor especifico
print(dados)

print(30*'-','x',30*'-')

del dados["ano"] # Excluindo chave ano
print(dados)

dados.clear() # Eliminar todos os items no dicionario
print(dados)

print(30*'-','x',30*'-')


dados = {"nome": "Grabriel", "ano": 1993, "valor_logico": True}
dados.update ({"estado": "Rio de Janeiro"})
print(f'Dicionario dados:{dados}')

for x in dados.values():
    print(x)

print(30*'-','x',30*'-')

for x in dados.keys():
    print(x)


print(30*'-','x',30*'-')    

for x, y in dados.items():
    print(x, y)    

print(30*'-','x',30*'-')    


# criei duas copias do dicionario dados.
dicio = dados.copy()
print(dicio)

print(30*'-','x',30*'-')

dicio2 = dict(dados)
print(dicio2)

print(30*'-','x',30*'-')

# aqui eu adicionei mais um elemento no dicionario dados.Os outros dois dicionarios continuaram como estavam antes, nao atualizaram 
dados["idade"]= 27
print(dados)
print(dicio)
print(dicio2)
