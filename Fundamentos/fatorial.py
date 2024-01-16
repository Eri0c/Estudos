"""
Como achar o fatorial de um numero
"""


numero = int(input(" Digite um número: "))

fatorial  = 1

if numero < 0:
    print("Não existe fatorial de numeros negativos")
elif numero == 0:
    print(f"O fatorial de {numero} é 1")
else:
    for x in range(1,numero+1):
        fatorial = fatorial*x
    print(f'O fatorial de {numero} é: {fatorial}')       