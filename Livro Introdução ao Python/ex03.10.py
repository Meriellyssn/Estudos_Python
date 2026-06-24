print('''Faça um programa que calcule o aumento de um salário. Ele deve 
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento 
e do novo salário''')
print('-=' * 20)

#Entrada de dados
salario = float(input('Digite o salário: R$ '))
porcentagem = float(input('Digite a porcentagem do aumento: '))

#Processamento (Lógica)
aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento
print('-=' * 20)
#Saída de dados
print(f'O aumento será de R$ {aumento:.2f}. O novo salário será de R$ {novo_salario:.2f}.')
