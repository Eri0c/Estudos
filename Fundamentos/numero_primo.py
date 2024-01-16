"""
descobrir se um numero é primo
"""

print(30 * "-")

numero = int(input("Digite um número para descobrir se o mesmo é primo: "))

if numero > 1:
    for x in range(2, numero):
        if(numero % x) == 0:
            print('Esse não é primo')
            break
    else:
        print('Esse numero é primo')
else:
    print('Esse numero não é primo: numero menor ou igual a 1')   
print( 30 * "-")
