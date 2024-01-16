# Argumentos nomeados

def imprimir_nome(nome, sobrenome, idade):
    print("Nome: ", nome)
    print("Sobrenome: ", sobrenome)
    print("Idade: ", idade)

print(30*'-', 'x', 30*'-')
# podemos utilizar variaveis fora do bloco da função
sobrenome = "clara"
idade = 35
# para isso devemos chamar da seguinte forma:
imprimir_nome(nome="Maria", sobrenome = sobrenome ,idade = idade)
# imprimir_nome(nome="Maria", sobrenome="Clara",idade=25) Desta forma pode ser possivel alterar a ordem.

print(30*'-', 'x', 30*'-')

imprimir_nome("Maria", "Clara", 25) 

