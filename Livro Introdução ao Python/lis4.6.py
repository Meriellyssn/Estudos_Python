print('Conta de telefone com três faixas de preços.')
print('-=' * 20)
minutos = int(input('Quantos minutos você utilizou esta mês: '))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.10
print('Você vai pagar este mês: R${:.2f}'.format(minutos * preco))
