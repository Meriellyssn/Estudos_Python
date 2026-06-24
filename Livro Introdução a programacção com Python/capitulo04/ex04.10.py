print('''Escreva um programa que calcule o preço a pagar pelo fornecimento 
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta
lação: R para residências, I para indústrias e C para comércios. Calcule o preço a 
pagar de acordo com a tabela a seguir.''')
print('-=' * 20)
kwh = float(input('Digite a quantidade de kWh consumida: '))
tipo = input('Digite o tipo de instalação (R, I ou C): ').upper().strip()[0]
tipo_valido = True
if tipo == 'R':
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65
elif tipo == 'C':
    if kwh <= 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
elif tipo == 'I':
    if kwh <= 5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
else:
    tipo_valido = False
    print('Erro: Tipo de instalação inválida! Por favor, digite R, I ou C.')
    
print('-=' * 20)
if tipo_valido:
    print(f'O preço a pagar é R$ {preco:.2f}')
else:
    print('Não foi possível calcular o preço devido ao tipo de instalação inválida.')