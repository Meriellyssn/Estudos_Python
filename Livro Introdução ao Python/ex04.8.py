print('''Escreva um programa que leia dois números e que pergunte qual 
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), 
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.''')
print('-=' * 20)

resultado = 0
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
operacao = str(input('Qual operação deseja realiza: [+], [-], [*] ou [/]? '))
operacao_valida = True
if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '*':
    resultado = n1 * n2
elif operacao == '/':
    if n2 == 0:
        operacao_valida = False
        print('Erro: Divisão por zero não é permitida!')
    else:
        resultado = n1 / n2
else:
    operacao_valida = False
    print('Opção inválida! Tente novamente.')
print('-=' * 20)
if operacao_valida:
    print(f'O resultado de {n1} {operacao} {n2} é igual a {resultado:.2f}!')
