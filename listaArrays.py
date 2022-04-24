#1
num = 0
lista = []
for i in range(99):
  lista.append(num)
  num = num + 1

print(lista)

#2
listaNotas = []
medianota = 0
for i in range(4):
  nota = float(input("Digite sua nota:"))
  medianota = medianota + nota
  listaNotas.append(nota)
print(medianota / len(listaNotas))

#3
notasAcima = []
for i in range(4):
  nota = float(input("Digite sua nota:"))
  if(nota >= 7):
    notasAcima.append(nota)

print(notasAcima)

#4
notasAbaixo = []
listaNotas = []
mediaturma = 0
notaB = 999999999
notaA = 0
for i in range(10):
  nota = float(input("Digite sua nota:"))
  if(nota <= 6):
    listaNotas.append(nota)
    notasAbaixo.append(nota)
    mediaturma = mediaturma + nota
  else:
    listaNotas.append(nota)
    mediaturma = mediaturma + nota
  if(nota < notaB):
    notaB = nota
  if(nota > notaA):
    notaA = nota

print("Media da turma:",mediaturma / len(listaNotas))
print("Notas Abaixo:",notasAbaixo)
print("Nota maior:",notaA,"Nota menor:",notaB)

#5
numLista = []
num = 0
numSearch = 0
for i in range(100):
  num = num + 1
  numLista.append(num)

for i in range(100):
  if(numLista[numSearch] == 30):
    search = numSearch
  else:
    numSearch = numSearch + 1

print(search)

#6
numLista = []
num = 0
somaLista = 0

for i in range(100):
  num = num + 1
  numLista.append(num)

for i in range(len(numLista)):
  somaLista = somaLista + numLista[i]

print(somaLista)

#7
listaNum = []
num = -100
for i in range(201):
  listaNum.append(num)
  num = num + 1

n = len(listaNum)

for t in range(len(listaNum)):
  n = n - 1
  print(listaNum[n])

#8
listaNum1 = []
listaNum2 = []
listaNum3 = []
num = 1
t = 0
for i in range(5):
  listaNum1.append(num)
  listaNum2.append(num)
  listaNum3.append(listaNum1[i] + listaNum2[i])
  t = t + 1
  num = num + 1

print("Vetor 1:",listaNum1)
print("Vetor 2:",listaNum2)
print("Vetor 3:",listaNum3)

#15
vet = []
for i in range(21):
  vet.append(i)

print(vet)

#18
matriz = [["Linha 1",1,2,3,4,5,6,7,8,9,10],["Linha 2",1,2,3,4,5,6,7,8,9,10],["Linha 3",1,2,3,4,5,6,7,8,9,10],["Linha 4",1,2,3,4,5,6,7,8,9,10],["Linha 5",1,2,3,4,5,6,7,8,9,10]]
for i in range(5):
  print(matriz[i])




  
  
