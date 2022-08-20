# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.
class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
    def __str__(self):
        return f'TAMANHO: {self.tamanho}\nINTERFACE: {self.interface}'
class MP3Player(Smartphone):
    def __init__(self,tamanho,interface):
        Smartphone.__init__(self, tamanho, interface)
    def __str__(self):
        return f'TAMANHO: {self.tamanho}\nINTERFACE: {self.interface}'
celular1 = Smartphone("3.5'",'Android')
celular2= Smartphone("2.7'",'IOS')
ipod = MP3Player("1.8'",'IOS')
print(celular1)
print(celular2)
print(ipod)