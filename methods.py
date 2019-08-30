from matplotlib import pyplot as plt
import numpy as np

def dist(qg,qn):
	distancia = (int(qg[0])-int(qn[0]))**2 + (int(qg[1])-int(qn[1]))**2
	return distancia

def field(qg):
	k = 9*1e9
	return k*int(qg)

def forca(campo,qn,distancia):
	return campo*int(qn)/distancia

