#Introdução ao POO
#Definindo a classe, seus atributos e seus métodos 
class Quadrado():
  def __init__(self, lado = 5):
    self.lado = lado
  def mostrarlado(self):
    return self.lado
  def area(self):
    return self.lado**2
  def perimetro(self):
    return self.lado * 4
  def setLado(self,novolado):
    self.lado = novolado

#Instanciando um objeto
qdr = Quadrado(lado = 7)
print('O lado do quadrado vale ',qdr.lado, '\nsua área vale ', qdr.area(),'\ne seu perimetro vale',qdr.perimetro(),'.')
