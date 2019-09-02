from matplotlib import pyplot as plt
import numpy as np

def graf(coord,coordG,f):
	dx = []	#Lista utilizada para variação do eixo X para criar a seta
	dy = []	#Lista utilizada para variação do eixo Y para criar a seta
	fig = plt.figure()	#Cria um objeto figura e o armazena na variável fig
	ax = fig.add_subplot(111) #Cria um espaço em uma matriz para gerar a imagem
	ax.grid(True)	#Define como verdadeiro a grade para melhor visualização
	ax.set_axisbelow(True)	#Coloca os eixos X e Y abaixo dos pontos
	ax.spines['left'].set_position('zero')	#Esta parte do código utiliza o método spines para gerar os eixos na origem
	ax.spines['right'].set_color('none')	
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.set_xticks(np.arange(-100,101,1)) #Cria marcadores a cada 1 unidade de medida nos eixos X e Y
	ax.set_yticks(np.arange(-100,101,1))
	
	ax.set_title("Gráfico das forças em relação à carga geradora.") #Define um título ao gráfico

	
	coord = np.array(coord)	#Transforma a lista coordenadas em matriz do numpy para trabalhar melhor
	x = coord[:,0]	#Separa as coordenadas de todas as cargas em X e Y
	y = coord[:,1] 	
	ger_x = float(coordG[0]) #Separa as coordenadas da carga geradora em X e Y
	ger_y = float(coordG[1])
	x = [float(i) for i in x] #Transforma todas as coordenadas para valores inteiros, já que foram lidas 
	y = [float(i) for i in y]	#no formato string
	
	plt.scatter(ger_x,ger_y, marker = 'P', s=200, c = 'Green') #Cria o Gráfico de dispersão para a carga geradora
	plt.scatter(x,y, s = 150)	#Cria o Gráfico de dispersão para todas as outras cargas

	for i in range(len(coord)):  	#Este bloco calcula o dx e dy para a direção das setas
		if f[i] < 0:				#As setas serão criadas a partir de x e y como posições iniciais
			dx.append(ger_x-x[i])	#E sua posição final será ((x+dx),(y+dy))
			dy.append(ger_y-y[i])

		elif f[i] > 0:
			dx.append(x[i] - ger_x)
			dy.append(y[i] - ger_y)
		else:
			dx.append(0)
			dy.append(0)

	for i in range(len(x)): #Gera as setas
		plt.arrow(x[i],y[i],dx[i]/2,dy[i]/2, head_width=0.1, head_length=0.1, color = 'Red', length_includes_head = True)
	
	f = ['%.2e' % abs(x) for x in f] #Transforma a força para notação cientifica
	for i in range(len(x)): #Cria a 'anotação' das forças nos pontos
		ax.annotate(r'$\vec f_{}$ = {}N'.format(i+1,f[i]),xy = (x[i],y[i]), color = 'black',  ha='right', va='bottom')
		print('q{} sofre uma força de: {}N'.format(i+1,f[i]))
	plt.show()	#Mostra o gráfico