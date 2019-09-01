from matplotlib import pyplot as plt
import numpy as np

def dist(qg,qn):
	distancia = (int(qg[0])-int(qn[0]))**2 + (int(qg[1])-int(qn[1]))**2#Cálculo da distância entre dois pontos, sem tirar a raiz, pelo fato do cálculo da força ter a distância ao quadrado, assim cortando a raiz
	return distancia

def field(qg):
	k = 9*1e9
	return k*int(qg)#Cálculo do campo em relação a carga geradora, sem a distância, pois ela varia para cada carga

def forca(campo,qn,distancia):
	if distancia == 0:
		print('Erro: Duas cargas não podem ocupar a mesma posição')
		exit()
	return campo*int(qn)/distancia#Cálculo da força entre a carga geradora e cada carga qn