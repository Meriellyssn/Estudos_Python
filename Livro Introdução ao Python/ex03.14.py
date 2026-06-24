print('''Escreva um programa que pergunte a quantidade de km percorridos 
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais 
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por 
dia e R$ 0,15 por km rodado.''')
print('-=' * 20)

#Entrada de Dados
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))

#Processamento de Dados
preco = (dias * 60) + (km * 0.15)

#Saída de Dados
print(f'O total a pagar é de R${preco:.2f}')
