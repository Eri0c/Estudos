# parametros para função
# passando valores do bloco interno para o bloco externo
def minha_funcao():
    var = "maria"
    return var


print(minha_funcao())
# var = maria_funcao()   outra forma de chamar a função
var = "ana"
print(var)

print(30*'-' , 'x' , 30*'-' )
# passando valores do bloco externo para bloco interno.

def nome_da_funcao(parametro): # parametro é o nome dado aos valores utilizados na definicao de uma função
    #corpo da função - identação
    print("Olá ",parametro)

nome = input("Qual seu nome? ")
nome_da_funcao(nome)   # argumento é o nome dado aos valores utilizados na chamada de uma função 
                       # o numero de argumento tem que acompanhar o numero de parametros


print(30*'-' , 'x' , 30*'-' )

def imprime_nome(nome): # nomes iguais tanto no parametro quanto na variavel para que fique isplixito 
    print("Olá, ", nome)


nome = "maria"
imprime_nome(nome)

print()
imprime_nome()