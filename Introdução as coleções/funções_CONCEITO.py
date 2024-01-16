# paradigma imperativo
# imperare
# variáveis, atribuições e principalmente sequêncial
#C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2
# função tem intuito de executar uma tarefa especifica 
# uma função é um bloco de codigo, uma sequencia de comandos que recebe um nome e pode ser chamada de qualquer lugar do codigo

nome = "Gabriel" # variável global é quando esta fora de uma função
#bloco externo


def minha_funcao(): # parenteses podem passar argumentos.
    # Bloco interneo *bloco interno de uma função é conhecido como corpo da função
    nome = "Ana" # variável local.
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("Impressão do bloco interno da condição if")
    for x in tupla:
        print(x)    
# tudo isso pode ser executado dentro de uma função. 


minha_funcao()# chamar a função
print(nome)

print(30*'-','x',30*'-')

    