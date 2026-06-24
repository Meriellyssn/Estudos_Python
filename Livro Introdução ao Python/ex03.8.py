print('''Escreva um programa que leia um valor em metros e o exiba con
vertido em milímetros.''')
print('-=' * 20)
n = float(input('Digite o valor em metros que deseja converter para cm: '))
conversor = n * 100
print('-=' * 20)
print(f'{n}m convertido é igual a {conversor:.2f}cm')
