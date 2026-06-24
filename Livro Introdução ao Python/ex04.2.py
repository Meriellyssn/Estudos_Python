print('''Escreva um programa que pergunte a velocidade do carro de um 
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário 
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 
80 km/h''')
print('-=' * 20)
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Você foi MULTADO em R${multa:.2f}, por estar acima da velocidade permitida!')
else:
    print('Tenha um Bom Dia! Dirija com Segurança!')
