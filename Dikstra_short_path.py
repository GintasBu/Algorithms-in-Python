import pickle
from heap import *
import copy
import os

D=pickle.load(open('Dikstra.p','rb'))
Dl={}
Di={}
for i in D:
	Dl[i]=False
	Di[i]=0

	
X=[]			# vertexes processed so far
vertex=1
X.append(vertex)	# start from vertex Nr 1
Dl[vertex]=True
while len(X)<200:
	Di0={}
	p=[]
	for i in X:		# scaning from X
		# possible nodes ending at:
		Y=D[i].ar
		z=0
		for z in range(len(Y)):
			#print 'z',z, 'Y', Y
			if Dl[Y[z][0]]==False:
				#Di0[Y[z][0]]=Di[Y[z][0]]+Y[z][1]+Di[i]
				p0=(Di[Y[z][0]]+Y[z][1]+Di[i], Y[z][0])
				p.append(p0)
				#print 'z',z, 'Y', Y, Y[z], 'i', i, p
	
	
	p=sorted(p, key=lambda x: x[0])
	#Di0[Y[z][0]]
	Di0[p[0][1]]=p[0][0]
	new=min(Di0.items(), key=lambda x: x[1])
	newvertex=new[0]
	
	#print 'newvertex', newvertex
	#print 'Di0', Di0
	Dl[newvertex]=True
	#if Di[newvertex]>0:
	#
	#if Di[newvertex]
	Di[newvertex]=Di[newvertex]+new[1]
	#print 'X', X, 'Y',Y
	X.append(newvertex)
	#print 'X', X, 'Y',Y
	#print "Di", Di, 
	#os.system("pause")

#print Di, len(Di)
li=[7,37, 59, 82, 99, 115, 133, 165, 188, 197]
for b in li:
	print b, Di[b]


	
	