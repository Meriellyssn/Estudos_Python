print('''Escreva um programa que calcule o preço a pagar pelo fornecimento 
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta
lação: R para residências, I para indústrias e C para comércios. Calcule o preço a 
pagar de acordo com a tabela a seguir.
Preço por tipo e faixa de consumo
Tipo Faixa (kWh) Preço
Residencial Até 500 R$ 0,40
Acima de 500 R$ 0,65
Comercial Até 1000 R$ 0,55
Acima de 1000 R$ 0,60
Industrial Até 5000 R$ 0,55
Acima de 5000 R$ 0,60
''')
#Entrada de Dados
kwh = float(input('Digite a quantidade de kwh consumida: '))
tipo = str(input('Digite o tipo de instalação (R, I ou C): ')).upper().strip()[0]

#Processamento de Dados
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
    if kwh <=5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
else:
    tipo_valido = False
    print('Erro: Tipo de instalação inválida!')
print('-=' * 20)
#A proteção final:
#Saida de Dados
if tipo_valido:
    print(f'O preço a pagar é de R$ {preco:.2f}')
else:
    print(f'Não foi possivel calcular o preço devido ao erro no tipo de instalação.')
