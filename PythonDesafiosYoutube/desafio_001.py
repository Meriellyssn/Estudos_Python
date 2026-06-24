print('''Implemente uma funçao que calcule as raizes de uma equação quadratica.
Caso as raizes sejam complexas, returne uma mensagem informando isso. 
''')

def calcular_raizes(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return 'Raízes Complexas'
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    return f'Há duas raízes reais: {x1} e {x2}'

print(calcular_raizes(1, -4, 4))