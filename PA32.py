items = [map(int, x.split(' ')) for x in open('knapsack2.txt', 'r').read().split('\n')[0:-1]]
import numpy as np
def knapsack(items):
	V=items[0][0]
	n=items[0][1]
	Da_1=[0]*(V+1)
	Da1=[0]*(V+1)
	for i in range(n+1):
		for w in range(V+1):
			a=[]
			if w==0 or i==0:
				Da1[w]=0
			else:
				a.append(Da_1[w])
				if w-items[i][1]>=0:
					a.append(Da_1[w-items[i][1]]+items[i][0])
				else: a.append(0)
				Da1[w]=max(a)
		Da_1=list(Da1)
	return Da1[V]
	
#items=[[6,4], [3,4], [2,3],[4,2],[4,3]]
D=knapsack(items)
print D