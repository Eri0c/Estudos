valor_produto = float(input('Digite o valor do produto: R$'))
porcentagem = float(input('Qual o desconto do produto em porcentagem? '))
valor_do_desconto = (porcentagem / 100) * valor_produto 
valor = valor_produto - valor_do_desconto
print(f'O valor com desconto de R${valor_do_desconto} \n custará R${valor}')
