cliente = input("Digite o nome do cliente:")
qtd_livro = int(input("Digite a quantidade de Livro:"))
livro = input("Digite o nome do Livro:")
valor = float(input("Digite o Valor do Livro:"))
vendedor = input("Digite o nome do Vendedor:")
calculo_porcentagem = (37.83 / 100) * valor
comissao = calculo_porcentagem

print(f'Olá ({cliente}) sua compra de ({qtd_livro}) qtd do livro \n({livro}) por R$({valor:.2f}) foi efetuada com sucesso!')

print(f'Olá, ({vendedor}) você acaba de receber uma comissão de RS$({comissao:.2f})\n pela compra realizada pelo(a) cliente ({cliente}).')
