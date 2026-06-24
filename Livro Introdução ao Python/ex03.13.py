print('''Exercício 3.13 Escreva um programa que converta uma temperatura digitada em 
°C em °F. A fórmula para essa conversão é:
F=9×C/5 +32''')
print('-=' * 20 )

#Entrada de Dados
celsius = float(input('Digite a temperatura C°: '))

#Processamento de Dados
fahrenheit = (9 * celsius / 5) + 32

#Saída de Dados
print(f'A temperatura de {celsius:.1f} C°, convertida para Fahrenheit é {fahrenheit:.1f} F°')