#items = [map(int, x.split(' ')) for x in open('testPA4b.txt', 'r').read().split('\n')[0:-1]]
import numpy as np
import os
def Bellman_Ford(graph, s):			# s -starting vertex
	ngraph=np.array(graph[1:len(graph)])
	n=graph[0][0]
	A=np.zeros((n,n))
	print len(A), ngraph
	for i in range(n):

		if i==0: 
			A[i][s-1]=0
		
		for v in range(1,n+1):
			print 'v,i,s', v, i, s
			if v!=s:
				if i==0: 
					A[i,v-1]=float('+inf')
				else:
					incoming_edges=ngraph[np.in1d(ngraph[:,1], v)]
					print incoming_edges, 'ined'
					a=[]
					if len(incoming_edges)>0:
						
						for l in incoming_edges:
							a.append(A[i-1][l[0]-1]+l[2])
							#print 'a', a
					else: a.append(float('+inf'))
					print a
					A[i][v-1]=min(A[i-1][v-1], min(a))
			print A
			os.system('pause')
	return A

	
#items=[[5, 6],[1,2, 2], [1,4,4],[2,4,1],[2,3,2],[3,5,2],[4,5,4]]

A=Bellman_Ford(items, 8)
print A
Alast=A[len(A)-1]
Anextolast=A[len(A)-2]
O=0
for o in range(len(Alast)):
	O+=Alast[o]-Anextolast[o]

if O==0:
	print "no negative cycle"
else: 
	print 'has a negative cycle'