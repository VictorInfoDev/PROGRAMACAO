#1/c)

#2

class Usuario():
    primeiroNome = ""
    ultimoNome = ""

    def hello(self):
        return "Olá, " + self.primeiroNome


#3

usuario1 = Usuario()

usuario1.primeiroNome = "Jonnie"
usuario1.ultimoNome = "Bravo"

#4

hello = usuario1.hello()
print(hello)
