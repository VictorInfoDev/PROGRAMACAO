#1
#d)

#2
class Usuario():
  __primeiroNome = ""
  
  def setprimeiroNome(self, primeiroNome):
    self.__primeiroNome = primeiroNome

  def getprimeiroNome(self):
    return self.__primeiroNome

usuario1 = Usuario()
usuario1.setprimeiroNome("Joe")

print(usuario1.getprimeiroNome())

#3

class Empregado():
  nome = ""
  __salario = ""
  projeto = ""

  def settrabalho(self):
    return f"{self.nome} está trabalhando no projeto {self.projeto}"

  def mostrar(self):
    return f"{self.nome} possui salário de R${self.__salario}"

  def setsalario(self, salario):
    self.__salario = salario

colaborador = Empregado()
colaborador.nome = "Adelar"
colaborador.projeto = "Mysql"
colaborador.setsalario(3500.00)

print(colaborador.settrabalho())
print(colaborador.mostrar())

#4

class Robo():
  __nome = ""
  __ano_construcao = ""

  def setatribuir(self, nome, ano_construcao):
    self.__nome = nome
    self.__ano_construcao = ano_construcao

  def getdiga_alo(self):
    return f"{self.__nome} é de {self.__ano_construcao}"

delta = Robo()
delta.setatribuir(nome="Sky", ano_construcao="2019")

print(delta.getdiga_alo())

#5

class Laptop():
  __preco = ""
  
  def get_preco(self):
    return f"O preço do Laptop Samsung é {self.__preco}"

  def set_preco(self, preco):
    self.__preco = preco

samsung = Laptop()
samsung.set_preco(3999)

print(samsung.get_preco())

#6

class Pessoa():
  __primeiroNome = ""
  __ultimoNome = ""

  def get_primeiroNome(self):
    return f"{self.__primeiroNome}"
  
  def get_ultimoNome(self):
    return f"{self.__ultimoNome}"

  def set_primeiroNome(self, primeiroNome):
    self.__primeiroNome = primeiroNome

  def set_ultimoNome(self, ultimoNome):
    self.__ultimoNome = ultimoNome
    
homem = Pessoa()
homem.set_primeiroNome("João")
homem.set_ultimoNome("Carvalho")

print(homem.get_primeiroNome(), homem.get_ultimoNome())
