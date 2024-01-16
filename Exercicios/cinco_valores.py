# Aqui eu declarei as variaveis juntamente com a função input para pedir os valores para o usuario
valor1 = int(input("Digite o 1° valor: "))
valor2 = int(input("Digite o 2° valor: "))
valor3 = int(input("Digite o 3° valor: "))
valor4 = int(input("Digite o 4° valor: "))
valor5 = int(input("Digite o 5° valor: "))
    
     
    # Verificando o maior valor
    # iniciei com um if  trazendo o primeiro valor como o maior.
    
if valor1> valor2 and valor1 > valor3 and valor1> valor4 and valor1> valor5:
    print(" O maior valor digitado é: ",valor1)    
# se o primeiro valor nao for o maior, sera executado o laço de repetição dentro do else:    
else:    
    if valor2 > valor1 and valor2 > valor3 and valor2 > valor4 and valor2 > valor5:
        print ("O maior valor é o ", valor2)

      
    if valor3 > valor1 and valor3 > valor2 and valor3 > valor4 and valor3 > valor5:
        print("O maior valor digitado é: ", valor3)
    
    if valor4 > valor1 and valor4 > valor2 and valor4 > valor3 and valor4 > valor5:
        print("O maior valor digitado é: ", valor4)
    
    if valor5 > valor1 and valor5 > valor2 and valor5 > valor3 and valor5 > valor4:
        print("O maior valor digitado é:  ", valor5)

    



