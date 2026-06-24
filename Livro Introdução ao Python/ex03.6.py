print('''Escreva uma expressão que será utilizada para decidir se um aluno foi 
ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores 
que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma 
está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.''')
print('-=' * 20)
m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
m3 = float(input('Digite a terceira nota: '))
media = (m1 + m2 + m3)/3
print('-=' * 20)
if media >= 7:
    print(f'APROVADO! Com média {media:.2f}!')
else:
    print(f'REPROVADO! Com média {media:.2f}!')