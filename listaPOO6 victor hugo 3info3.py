class Usuario():
  __nomeUsuario = ""

  def setNome(self, nome):
    self.__nomeUsuario = nome

  def getNome(self):
    return self.__nomeUsuario

  
  
class Admin (Usuario):

  def escrevaNome(self):
    return "Admin"

  def digaOla(self):
    return "Olá " + self.escrevaNome() +", "+ self.getNome() 


usuario1 = Admin()
usuario1.setNome("Baltazar")
print(usuario1.digaOla())