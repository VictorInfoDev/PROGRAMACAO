#1
class Bola():
  cor = ""
  circuferencia = ""
  material = ""

  def mostrarCor(self):
    print("Cor: " + self.cor)

  def trocarCor(self, nova_cor):
    self.cor = nova_cor

    return self

bola1 = Bola()
bola1.cor = "Branca"
bola1.trocarCor("Verde")
bola1.mostrarCor()

#2
class Quadrado():
  lado = 0

  def mudarLado(self, novo_lado):
    self.lado = novo_lado
    
    return self

  def calcularArea(self):
    result = self.lado * self.lado
    print("Tamanho do lado: " + str(self.lado) + " Tamanho da área: " + str(result))

quadrado1 = Quadrado()
quadrado1.lado = 7
quadrado1.mudarLado(8)
quadrado1.calcularArea()

#4
class Pessoa():
  nome = ""
  idade = 0
  peso = 0
  altura = 0

  def envelhecer(self, anos):
    self.idade = self.idade + anos
    bonus = 0.05 * anos

    if (self.idade <= 21):
      self.altura = self.altura + bonus
    
    print("Idade: " + str(self.idade) + " Altura: " + str(self.altura))

  def engordar(self, pesos):
    self.peso = self.peso + pesos

    print("Peso: " + str(self.peso))

  def emagrecer(self,pesos):
    self.peso = self.peso - pesos

    print("Peso: " + str(self.peso))

  def crescer(self, medida):
    self.altura = self.altura + medida

    print("Altura: " + str(self.altura))

pessoa1 = Pessoa()
pessoa1.nome = "Jonnie"
pessoa1.idade = 18
pessoa1.peso = 70
pessoa1.altura = 1.85

pessoa1.envelhecer(3)
pessoa1.engordar(3)
pessoa1.emagrecer(1)
pessoa1.crescer(0.03)
