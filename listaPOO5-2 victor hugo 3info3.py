#1

class Usuario():
  __primeiroNome = ""
  __ultimoNome = ""

  def __init__(self, nome, nome2):
    self.__primeiroNome = nome
    self.__ultimoNome = nome2


  def getNomeCompleto(self):
    return "Nome: " + self.__primeiroNome + " " + self.__ultimoNome

  
usuario1 = Usuario("Johnny", "Bravo")
print(usuario1.getNomeCompleto())