class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'
    


meu_carro = Carro('Toyota', 'Prata')
print(meu_carro)