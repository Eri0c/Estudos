# maneira como a função devolve o resultado, com ou sem valor
# uma função deve ter um retorno.
lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop()
var1 = print("Olá mundo")
print(f'Retorno da função pop: {retorno}')
print('Retorno da função print:', var1) # retorno sem valor

print(30*'-','x',30*'-')

def ola_mundo(): # desta forma economizamos linhas
    return "ola mundo"
    

print(ola_mundo())
# outra forma de utilizar 
#retorno = ola_mundo()

# uma função não pode ser vazia.
print(30*'-','x',30*'-')

def par_impar():#pass# ignorando essa função para que possa testar o codigo antes de preencher esta função
    numero = 19
    if (numero % 2) == 0:
        return "Numero par" # return faz com que o laço seja interrompido apos ler o primeiro return correto.
    return "numero impar"
print("ola mundo")
print(par_impar())
print("ola mundo novamente")


x = 0
if x == 0:
    print("0")
print("ola")     


print(30*'-','x',30*'-')
