items = [map(int, x.split(' ')) for x in open('knapsack2.txt', 'r').read().split('\n')[0:-1]]
import numpy as np
import os

def knapsack(items):
	V=items[0][0]
	n=items[0][1]
	#items.pop(0)
	Da=np.zeros([n+1, V+1])
	for i in range(n+1):
		for w in range(V+1):
			a=[]
			if w==0 or i==0:
				Da[i][w]=0
			else:
				#print i, w, items[i][1]
				a.append(Da[i-1][w])
				if w-items[i][1]>=0:
					a.append(Da[i-1][w-items[i][1]]+items[i][0])
				else: a.append(0)
				Da[i,w]=max(a)
			#print Da, a
			#os.system('pause')
	return Da[n][V]
	
#items=[[6,4], [3,4], [2,3],[4,2],[4,3]]
D=knapsack(items)
print D