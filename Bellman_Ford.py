import numpy as np
def Bellman_Ford(graph, s):			# s -starting vertex
	ngraph=np.array(graph[1:len(graph)])
	n=graph[0][0]
	A=np.zeros((n,n))
	#print len(A)
	for i in range(n):
		if i==0: 
			A[i][s-1]=0
		for v in range(1,n+1):
			if v!=s:
				if i==0: 
					A[i,v-1]=float('+inf')
				else:
					incoming_edges=ngraph[np.in1d(ngraph[:,1], v)]
					a=[]
					if len(incoming_edges)>0:
						for l in incoming_edges:
							a.append(A[i-1][l[0]-1]+l[2])
					else: a.append(float('+inf'))
					A[i][v-1]=min(A[i-1][v-1], min(a))
	return A
	Alast=A[len(A)-1]
	Anextolast=A[len(A)-2]
	O=0
	for o in range(len(Alast)):
		O+=Alast[o]-Anextolast[o]
	if O==0:
		print "no negative cycle"
	else: 
		print 'has a negative cycle'