def grau(valor,v1,v2):
  for i in range(valor):
    v1.sort()
    v2.sort()
    if v1[i] != v2[i]:
       return "nao"
    
  return "sim"

def funcao(alf,num,lista,j,grau):
  a = lista[1:len(lista)]
  if alf in a:
    return grau[j]
  elif num in a:
    return grau[j]
  else:
    return 0

def repetido(lista):
  l = []
  c = 0
  for i in range(len(lista)):
    if lista[i] not in l:
      l.append(lista[i])
    else:
      c += 1
  
  return c

num = input()
num = num.split(' ')
num_grafo = list(map(int, num))

if num_grafo[0] != num_grafo[1]:
  print('nao')
else:
    mtx1 = [[0 for x in range(num_grafo[0])] for y in range(num_grafo[0])]
    mtx2 = [[0 for x in range(num_grafo[1])] for y in range(num_grafo[1])]

    vertg1 = []
    i = 0
    while(i < int(num_grafo[0])):
        vert = input()
        vertg1.append(vert)
        i += 1
  

    vertg2 = []
    o = 0
    while(o < int(num_grafo[1])):
        vert = input()
        vertg2.append(vert)
        o += 1

    vertg1.sort()
    vertg2.sort()

    grau_g1 = []
    for i in range(len(vertg1)):
        f = vertg1[i].split(' ')
        rep = repetido(f)
        if rep == 1:
            grau_g1.append(len(f))
        else:
            grau_g1.append(len(f) - 1)

    grau_g2 = []
    for i in range(len(vertg2)):
        f = vertg2[i].split(' ')
        rep = repetido(f)
        if rep == 1:
            grau_g2.append(len(f))
        else:
            grau_g2.append(len(f) - 1)

    alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']


    for i in range(num_grafo[0]):
        for j in range(num_grafo[0]):
            k = funcao(vertg1[j][0],num[j],vertg1[i],j,grau_g1)
            mtx1[i][j] = k

    for i in range(num_grafo[0]):
        for j in range(num_grafo[0]):
            k = funcao(vertg2[j][0],num[j],vertg2[i],j,grau_g2)
            mtx2[i][j] = k

    for i in range(len(mtx1)):
        mtx1[i].sort()

    for i in range(len(mtx2)):
        mtx2[i].sort()

    valor = grau(num_grafo[0],grau_g1,grau_g2)

    if valor == "nao":
        print("nao")
    else:
        contador = 0
        for i in range(len(mtx1)):
            if mtx1[i] not in mtx2:
                contador += 1 

        if contador == 0:
            print("sim")
        else:
            print("nao")