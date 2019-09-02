from matplotlib import pyplot as plt
import numpy as np

def dist(qg,qn):
	distancia = (float(qg[0])-float(qn[0]))**2 + (float(qg[1])-float(qn[1]))**2#Cálculo da distância entre dois pontos, sem tirar a raiz, pelo fato do cálculo da força ter a distância ao quadrado, assim cortando a raiz
	return distancia

def field(qg):
	k = 9*1e9
	return k*float(qg)#Cálculo do campo em relação a carga geradora, sem a distância, pois ela varia para cada carga

def forca(campo,qn,distancia):
	if distancia == 0:#Verifica se a carga qn e a geradora de campo estão na mesma posição
		print('Erro: Duas cargas não podem ocupar a mesma posição')
		exit()
	return campo*float(qn)/distancia#Cálculo da força entre a carga geradora e cada carga qn