#1
num = 0
numList = 0
lista = []
for i in range(99):
  num = num + 1
  lista.append(num)

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


