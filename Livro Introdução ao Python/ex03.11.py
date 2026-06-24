print('''Faça um programa que solicite o preço de uma mercadoria e o 
percentual de desconto. Exiba o valor do desconto e o preço a pagar.''')
print('-' * 20)

#Entrada de Dados
preco = float(input('Digite o valor do produto: R$ '))
porcentagem = float(input('Digite o percentual de desconto: '))

#Processamento (Lógica)
valor_desconto = preco * (porcentagem / 100)
preco_a_pagar = preco - valor_desconto

#Saída de Dados
print(f'O desconto é de R${valor_desconto:.2f}, e o preço a pagar é de R${preco_a_pagar:.2f}.')
