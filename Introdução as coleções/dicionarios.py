# listas: coleção ordenada, mutável e que permite valores suplicados
# tuplas: coleção ordenada, imutável e que permite valores duplicados
# Dicionarios: Coleção nao ordenada, mutavel e que nao permite valores duplicados.
# dicionario nao possui index;
# dicionario  funciona como chave:valor
dicio = {"chave1": "Gabriel","chave2": 1993, "chave3": True}
print(dicio)

print(60*'-')

dicionario = {
    "nome": "Bruna",
    "idade": 27,
    "nacionalidade": "brasileira",
}

print(dicionario)

print(60*'-')

print(dicionario["nacionalidade"])# chamando uma chave especifica

print(60*'-')

print(dicionario.get("nome"))# chamando uma chave especifica

print(dicionario.keys())

print(60*'-')

print(len(dicionario))

print(60*'-')

print(dicionario.values())

print(60*'-')

if "idade" in dicionario:
    print("A chave idade existe")

print(60*'-')

print(dicionario.items())

