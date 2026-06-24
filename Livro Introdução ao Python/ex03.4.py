print('''Escreva uma expressão para determinar se uma
pessoa deve ou não pagar imposto. Considere que
pagam imposto pessoas cujo salário é maior que R$ 1.200,00''')
print('-=' * 20)
while True:
    salario = float(input('Digite seu salário: R$ '))
    if salario > 1200:
        print('Você precisa pagar imposto!')
        print('-=' * 20)
    else:
        print('Você não precisa pagar imposto!')
        print('-=' * 20)
    sair = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('-=' * 20)
print('FIM DO PROGRAMA')