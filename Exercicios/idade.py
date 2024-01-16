idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Menor de idade')
elif idade >= 16 and idade <= 18:
    print('Emancipado')
else:
    print('Maior de idade')

