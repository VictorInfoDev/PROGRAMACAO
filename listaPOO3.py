#1.1, 1.2, 1.3, 1.4, 1.5

class Usuario():
  primeiroNome = ""

  def hello(self):
    print("Olá, " + self.primeiroNome)
    return self

  def registrar(self):
    print(">> registrado")
    return self

  def mail(self):
    print(">> e-mail enviado")

usuario1 = Usuario()
usuario1.primeiroNome = "Jane"
usuario1.hello().registrar().mail()

#2

class Carro():
  veiculo = ""

  def ligar(self):
    print(">> Carro Ligado")
    return self

  def dirigir(self):
    print(">> Andando...")
    return self

  def frear(self):
    print(">> O carro parou")
    return self

  def desligar(self):
    print(">> Carro Desligado")

ford = Carro()
ford.veiculo = "focus"

ford.ligar().dirigir().frear().desligar()
