#1/a)
#2/a)
#3/b)
#4/a)
#5
#Nome da classe: Usuario
#Propriedade: nome, sobrenome
#Método: cumprimentar

#6
class Usuario():
  nome = ""
  sobrenome = ""

  def cumprimentar(self):
    return "Olá"

#7
usuario1 = Usuario()

#8
usuario1.nome = "João"
usuario1.sobrenome = "Pedro"

#9
print(usuario1.nome, usuario1.sobrenome)

#10
hello = usuario1.cumprimentar()

print(hello, usuario1.nome, usuario1.sobrenome)

#11
usuario2 = Usuario()

usuario2.nome = "Jane"
usuario2.sobrenome = "Silva"

print(hello, usuario2.nome, usuario2.sobrenome)
