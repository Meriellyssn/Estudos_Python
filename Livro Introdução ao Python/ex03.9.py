print('''Escreva um programa que leia a quantidade de dias, horas, minutos 
e segundos do usuário. Calcule o total em segundos.''')
print('-=' * 20)
dias = int(input('Digite quantos dias: '))
horas = int(input('Digite quantas horas: '))
minutos = int(input('Digite quantos minutos: '))
segundos = int(input('Digite quantos segundos: '))
minutos_segundos = minutos * 60
horas_segundos = horas * 3600
dias_segundos = dias * 86400
soma = minutos_segundos + horas_segundos + dias_segundos + segundos
print('-=' * 20)
print(f'O total calculado é de {soma} segundos.')