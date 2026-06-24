print('''Escreva um programa que leia três números e que imprima o maior e o menor.''')
print('-=' * 20)

#Entrada de Dados
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

# Estratégia do Campeão (Lógica)
menor = n1
maior = n1

#Testando o menor
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

#Testando o maior
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('-=' * 20)

#Saída de Dados
print(f'O maior valor digitado foi >> {maior}')
print(f'O menor valor digitado foi >> {menor}')
