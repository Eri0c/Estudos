"""
Escreva um programa para calcular as somas:
 S = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1
 S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)
 S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)
 """

def soma_sequencia1(n):
    soma = 0
    numerador = 3
    for i in range(n):
        denominador = 40 - i
        soma += numerador / denominador
        numerador += 1
    return soma

# Função para calcular a soma da segunda sequência
def soma_sequencia2(n):
    soma = 0
    numerador = 480
    for i in range(n):
        denominador = 2 + 22*i
        soma += numerador / denominador
        numerador -= 5
    return soma

# Função para calcular a soma da terceira sequência
def soma_sequencia3(n):
    soma = 0
    numerador = 1
    for i in range(n):
        denominador = 2 + 2*i
        soma += numerador / denominador
        numerador = 2*numerador + 1
    return soma

# Número de termos desejados
n = 20

# Calcular e imprimir as somas
soma1 = soma_sequencia1(n)
soma2 = soma_sequencia2(n)
soma3 = soma_sequencia3(n)

print("Soma da primeira sequência:", soma1)
print("Soma da segunda sequência:", soma2)
print("Soma da terceira sequência:", soma3)

