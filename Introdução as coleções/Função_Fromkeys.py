# retorna valor como chaves, que podem ser usados para criar dicionarios a partir de listas ou tuplas

tupla = ("item1", "item2", "item3")
x = 0 # a partir disso todos os elementos das minha chaves possuem o valor 0

dicio = dict.fromkeys(tupla, x)
print(dicio)

print(30*'-','x',30*'-')

tupla = ("item1", "item2", "item3")
tupla2 = ("item1", "item2", "item3")
dicio = dict.fromkeys(tupla, tupla2)
print(dicio)

print(30*'-','x',30*'-')

# Alinhamento de dicionarios

dicio = {
    "dicio1": {
        "nome": "Ana",
        "idade": 25,
    },
    "dicio2": {
        "nome": "Pedro",
        "idade": 38,
        "dicio3": {
            "nome": "Ana Julia",
            "idade": 5,
        }

    }
}

print(dicio)

