print('''Escreva um programa que pergunte o salário do funcionário e calcule 
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 
10%. Para os inferiores ou iguais, de 15%.''')
print('-=' * 20)
salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    aumento = salario * 0.10 #10% (10/100)
else:
    aumento = salario * 0.15 #15% (15/100)
novo_salario = salario + aumento
print(f'O valor do seu aumento é de R${aumento:.2f}. O seu novo salário será de R${novo_salario:.2f}.')
