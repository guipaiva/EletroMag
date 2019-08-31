from matplotlib import pyplot as plt
import numpy as np

def graf(coord,coordG,f):
	dx = []
	dy = []
	
	fig = plt.figure() 		
	ax = fig.add_subplot(111)
	ax.grid(True)
	ax.set_axisbelow(True)
	ax.spines['left'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.set_xticks(np.arange(-100,101,1))
	ax.set_yticks(np.arange(-100,101,1))
	
	ax.set_title("Gráfico das forças em relação à carga geradora.")

	
	coord = np.array(coord)
	x = coord[:,0]
	y = coord[:,1]
	ger_x = int(coordG[0])
	ger_y = int(coordG[1])
	x = [int(i) for i in x]
	y = [int(i) for i in y]
	
	plt.scatter(ger_x,ger_y, marker = 'P', s=200, c = 'Green', zorder=1)
	plt.scatter(x,y, s = 150)# marker= r"$ q{}$".format(i+1))

	for i in range(len(coord)):
		if f[i] < 0:
			dx.append(ger_x-x[i])
			dy.append(ger_y-y[i])

		elif f[i] > 0:
			dx.append(x[i] - ger_x)
			dy.append(y[i] - ger_y)
		else:
			dx.append(0)
			dy.append(0)

	for i in range(len(x)):
		plt.arrow(x[i],y[i],dx[i]/2,dy[i]/2, head_width=0.1, head_length=0.1, color = 'Red', length_includes_head = True, zorder=2)
	
	f = ['%.2e' % abs(x) for x in f]
	for i in range(len(x)):
		ax.annotate(r'$\vec f_{}$ = {}C'.format(i+1,f[i]),xy = (x[i],y[i]), color = 'black',  ha='right', va='bottom')
		print('q{} sofre uma força de: {}C'.format(i+1,f[i]))
	plt.show()

