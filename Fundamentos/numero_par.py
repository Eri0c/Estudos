"""
Como descobrir se um numero é impar ou par


num = 5
numero = 2

print(5/2)

#0,2,44,6,8,10,12,14...
#0/2,2/2,4/2... (ESSES NUMEROS SAO MULTIPLOS DE DOIS, divisiveis por 2) divisao inteira, nao tem resto
"""
print( 30 * '-')

while True:
    
    numero = int(input("Digite um numero para saber se o mesmo eh par: "))
    if (numero % 2) == 0:
        print(f"{numero} eh um numero par")
        break
    else:
        print(f"{numero} eh impar")
else: 
    print("Erro na aplicação")
    print(bool(numero))
print( 30 * '-')        
    
      

      