from methods import *
import numpy
import plot



n = int(input("Digite o número de cargas a ser inseridas: "))
cargas = []
coordenadas = []
distancias = []
forcas = []
for i in range(n):
	print("Digite o valor da carga {} em Coulombs: ".format(i+1),end=' ')
	cargas.append(input())
	print("Digite a posição X,Y da carga {}: ".format(i+1))
	coord = input().split(',')
	coord[0] = coord[0][1:]
	coord[1] = coord[1][:-1]
	coordenadas.append(tuple(coord))


indice = int(input("Digite qual a carga geradora: "))

c_geradora = cargas.pop(indice-1)

coord_geradora = coordenadas.pop(indice-1)

campo = field(c_geradora)

for i in range(len(coordenadas)):
	distancias.append(dist(coord_geradora,coordenadas[i]))
	forcas.append(forca(campo,cargas[i],distancias[i]))


forcas = ['%.3e' % x for x in forcas]
print(forcas)
