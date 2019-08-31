from methods import *
import numpy as np
from plot import graf
import time

try:
	n = int(input("Digite o número de cargas a ser inseridas (Mínimo duas cargas):"))
except ValueError:
	print('Número inválido, encerrando o programa...')
	time.sleep(3)
	exit()
else:
	if n <= 1:
		print('Número inválido, encerrando o programa...')
		time.sleep(3)
		exit()
	


n = int(n)
cargas = []
coordenadas = []
distancias = []
forcas = []
for i in range(n):
	print("Digite o valor da carga {} em Coulombs: ".format(i+1),end=' ')
	cargas.append(input())
	print("Digite a posição da carga {} no formato (X,Y): ".format(i+1))
	coord = input().split(',')
	coord[0] = coord[0][1:]
	coord[1] = coord[1][:-1]
	coordenadas.append(coord)

indice = int(input("Digite qual a carga geradora: "))

c_geradora = cargas.pop(indice-1)

coord_geradora = coordenadas.pop(indice-1)
campo = field(c_geradora)

for i in range(len(coordenadas)):
	distancias.append(dist(coord_geradora,coordenadas[i]))
	forcas.append(forca(campo,cargas[i],distancias[i]))

graf(coordenadas, coord_geradora,forcas)


