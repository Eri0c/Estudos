# Codigo par adivinhar um numero
# Do while

palpite = 5
numero = 9


while True: # Executamos sem verificar
    print("Qual o numero correto? ")
    palpite = int(input())
    if palpite == numero: # Estamos verificando nosso codigo
        print("Parabens voce acertou")
        break
    else:
        print("Voce errou")
else:  # Essas duas linhas ficam para area de teste. somente os desenvolvedores visualizam
    print("Erro na aplicação")
    print(bool(palpite))
    