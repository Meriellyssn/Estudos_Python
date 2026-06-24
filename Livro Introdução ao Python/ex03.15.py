print('''Escreva um programa para calcular a redução do tempo de vida de 
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos 
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, 
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.''')
print('-=' * 20)
#Entrada de Dados
quant_cigarros = int(input('Qual a média de cigarros por dia? '))
anos = int(input('A quanto tempo você fuma? '))

#Processamento de Dados
total_cigarros = quant_cigarros * 365 * anos
total_minutos = total_cigarros * 10
dias_perdidos = total_minutos / 1440

#Saída de Dados
print(f'Uma pessoa que fumou {total_cigarros} cigarros ao longo de {anos} anos, '
      f'perdeu {dias_perdidos:.0f} dias da sua vida!')