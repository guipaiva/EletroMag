from matplotlib import pyplot as plt
import numpy as np

def graf(coord,coordg):
	
	coord.sort(key=lambda x: x[0])
	fig = plt.figure() 		
	'''ax = fig.add_subplot(111)
	ger_x = coordg[0]
	ger_y = coordg[1]'''
	coord = np.array(coord)
	x = coord[:,0]
	y = coord[:,1]
	plt.scatter(x,y)
	plt.show()

