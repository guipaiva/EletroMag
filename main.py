from methods import *
import numpy as np
from plot import graf
import time

try:
	n = int(input("Digite o número de cargas a ser inseridas (Mínimo duas cargas): "))
except ValueError:#Retorna essa mensagem e encerra o programa caso alguém digite uma letra 
	print('Número inválido, encerrando o programa...')
	time.sleep(3)
	exit()
else:
	if n <= 1:#Retorna essa mensagem e encerra o programa caso alguém digite uma letra 
		print('Número inválido, encerrando o programa...')
		time.sleep(3)
		exit()
	

n = int(n)
#Listas usadas para armazenar dados e utilizá-los ao longo dos cálculos 
cargas = []#Armazena as cargas de cada carga
coordenadas = []#Armazena as coordenadas das cargas
distancias = []#Armazena a distância entre as cargas e a carga geradora do campo
forcas = []#Armazena as forças de cada carga em relação a carga geradora de campo
for i in range(n):
	print("Digite o valor da carga {} em Coulombs: ".format(i+1),end = ' ')
	cargas.append(input())#Armazena o valor da carga na lista cargas
	print("Digite a posição da carga {} no formato (X,Y): ".format(i+1),end = ' ')
	coord = input().split(',')#Recebe o valor da coordenada no formato (X,Y) e remove a vírgula armazenando dois valores '(x' e 'y)'
	coord[0] = coord[0][1:]#Remove o ( do valor '(x', para só o inteiro de x
	coord[1] = coord[1][:-1]#Remove o ) do valor 'y)', para só o inteiro de y
	coordenadas.append(coord)#Armazena os inteiro x e y como vetores de duas posições na lista coordenadas

indice = int(input("Digite qual a carga geradora: "))

c_geradora = cargas.pop(indice-1)#Armazena o valor da carga escolhida como geradora nessa variável e remove da lista cargas

coord_geradora = coordenadas.pop(indice-1)#Armazena o valor do vetor da coordenada da carga escolhida como geradora nesse vetor e remove da lista cargas
campo = field(c_geradora)#Chama a função que calcula o campo da carga geradora

for i in range(len(coordenadas)):
	distancias.append(dist(coord_geradora,coordenadas[i]))#Chama a função que calcula as distâncias
	forcas.append(forca(campo,cargas[i],distancias[i]))#Chama a função que calcula as forças

print('Campo gerado: {:.2e}/dist²N/C'.format(abs(campo)))
graf(coordenadas, coord_geradora,forcas)#Chama a função que plota o gráfico
