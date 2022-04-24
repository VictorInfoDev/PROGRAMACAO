#1
def converter(Fah):
  result = (Fah - 32) * 5 / 9
  return result

Celsius = converter(68)
print(Celsius)

#2
def conta(ctA, ctB):
  result = (ctA ** 2 + ctB ** 2) ** (1/2)
  return result

hipotenusa = conta(12 ,4)
print(hipotenusa)

#3
def conta(notaA, notaB):
  contaMedia = (notaA + notaB) / 2
  if(contaMedia >= 6):
    msg = "PARABÉNS! Você foi aprovado!"
  if(contaMedia < 6):
    msg = "Em exame..."
  
  return msg
  
media = conta(7, 8)
print(media)

#4
def conta(sexo, altura):
  if(sexo == "Homem" or "homem"):
    result = (72.7 * altura) - 58
  if(sexo == "Mulher" or "mulher"):
    result = (62.1 * altura) - 44.7
  
  return result

pesoideal = conta("Homem", 1.88)
print("Seu peso ideal é:", round(pesoideal))

#5
def conta(lados, medida):
  result = lados * medida
  if(lados == 3):
    print("TRIÂNGULO")
  if(lados == 4):
    print("QUADRADO")
  if(lados == 5):
    print("PENTÁGONO")
    
  return result

poligono = conta(5, 7)
print(poligono,"cm")

#6
def conta(n1, n2):
  total = 0
  if(n1 > n2):
    n2 = n2 + 1
    while(n1 > n2):
      n1 = n1 - 1
      total = total + n1
  if(n2 > n1):
    n1 = n1 + 1
    while(n2 > n1):
      n2 = n2 - 1
      total = total + n2

  print(total)

result = conta(5 , 2)

#7
def calendario(num):
  if(num == 1):
    print("Janeiro")
  if(num == 2):
    print("Fevereiro")
  if(num == 3):
    print("Março")
  if(num == 4):
    print("Abril") 
  if(num == 5):
    print("Maio") 
  if(num == 6):
    print("Junho") 
  if(num == 7):
    print("Julho") 
  if(num == 8):
    print("Agosto") 
  if(num == 9):
    print("Setembro") 
  if(num == 10):
    print("Outubro") 
  if(num == 11):
    print("Novembro") 
  if(num == 12):
    print("Dezembro")     
  if(num > 12 or num < 1 ):
    print("Mês inválido!")

mes = calendario(7)

#8
def semana(num):
  if(num == 1):
    print("DOM")
  if(num == 2):
    print("SEG")
  if(num == 3):
    print("TER")
  if(num == 4):
    print("QUA")
  if(num == 5):
    print("QUI")
  if(num == 6):
    print("SEX")
  if(num == 7):
    print("SAB")
  if(num > 7 or num < 1):
    print("Dia da semana inválido.")

dia = semana(7)