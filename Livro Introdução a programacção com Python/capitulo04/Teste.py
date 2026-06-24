valores = (int(input('Digite o 1º valor: ')),
           int(input('Digite o 2º valor: ')),
           int(input('Digite o 3º valor: ')),
           int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores: {valores}')
#A) Quantas vezes apareceu o valor 9.
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
#B) Em que posição foi digitado o primeiro valor 3.
if 3 in valores:
    print(f'O valor 3 apareceu na posição {valores.index(3)}º.')
else:
    print('O valor 3 não foi digitado.')
#C) Quais foram os números pares digitados.
print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
