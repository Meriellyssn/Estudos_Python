class Veiculo:
    def __init__(self, cor, placa, numeros_rodas):
        self.cor = cor
        self.placa = placa
        self.numeros_rodas = numeros_rodas
    
    def ligar_motor(self):
        print('Ligando o motor')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhão(Veiculo):
    def __init__(self, cor, placa, numeros_rodas, carregado):
        super().__init__(cor, placa, numeros_rodas)
        self.carregado = carregado
    
    def status(self):
        print(f'{'Sim' if self.carregado else 'Não'} esta carregado')


moto = Motocicleta("Preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro('Branco', 'xcv-9631', 4)
carro.ligar_motor()

caminhao = Caminhão('Azul', 'azs-1478', 8, True)
caminhao.ligar_motor()
caminhao.status()
print('-=' * 20)
print(caminhao)
