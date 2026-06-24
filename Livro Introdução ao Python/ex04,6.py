print('''Escreva um programa que pergunte a distância que um passageiro 
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km 
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.''')
print('-=' * 20)

#Entrada de Dados
distancia = float(input('Qual a distância da sua viagem em KM? '))

#Processamento de Dados
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

#Saída de Dados
print(f'O valor da sua passagem será de R$ {preco:.2f}. Tenha uma boa viagem!')
