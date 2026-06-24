print('''Escreva um programa para aprovar o empréstimo bancário para 
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o 
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser 
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da 
casa a comprar dividido pelo número de meses a pagar.''')
#Entrada de Dados
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos a pagar: '))

#Processamento de Dados
prestacao = casa / (anos * 12)
minimo = salario * 0.30 #Regra de Negocio, a parcela não pode ser superior a 30 % do salario.

#Saida de Dados
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}.')
if prestacao <= minimo:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')
