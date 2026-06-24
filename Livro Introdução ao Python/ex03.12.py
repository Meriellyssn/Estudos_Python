print('''Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro. 
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.''')
print('-=' * 20)

#Entrada de Dados
distancia = float(input('Qual a distância a ser percorrida? '))
velocidade = float(input('Qual a velocidade média para a viajem? '))

#Processamento (Lógica)
tempo = distancia / velocidade

#Saída de Dados
print(f'O tempo de viagem será aproximadamente de {tempo:.2f} horas.')
