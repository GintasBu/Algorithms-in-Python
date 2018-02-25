import numpy as np
import copy
items = [map(int, x.rstrip().split(' ')) for x in open('PA22test1.txt', 'r').read().split('\n')[0:-1]]
N=len(items)
D=dict()
i=0
duplic=set()
for x in items:
    #xx=''.join(x)
    b=int(''.join(map(str, x)),2)
    a=sum(x)
    if (a,b) not in D:
        D[(a,b)]=np.array(x)
    else: 
        i+=1
        print 'repeated key', i, (a,b), x
        duplic.add((a,b))

		
def mapin(item):
    dif=D[st]!=D[item]
    if sum(dif)<3:
        ls.add(item)


def findsets(D):
    L=sorted(D.keys())
    jj=0
    LL=[]
    global st, ls
    while len(L)>0:
        
        ls=set()
        st=L.pop(0)
        ls.add(st)
        shL=[item for item in L if item[0] >=st[0] and item[0]<st[0]+3]
        #global st, ls
        map(mapin, shL)
        #for item in shL:
        #    dif=D[st]!=D[item]
        #    if sum(dif)<3:
        #        ls.add(item)
        LL.append(ls)
        if len(LL)%100==0: print len(LL), st
    return LL
	
	
import numpy as np


class UnionFind:
	def __init__(self, n):
		if type(n)==type([]):
			self.node=[np.array(0)]*len(n)
			self.lenn=np.ones(len(n), dtype=int) #*len(n)
			self.parent=np.ones(len(n), dtype=int)
			self.name=[(1,1)]*len(n)
			#self.summ=np.ones(len(n),dtype=int)
			for i in n:
				self.node[i]=np.array(range(24))
				self.parent[i]=i
				
		else: 
			self.node=np.zeros(1)+n
			self.parent=np.zeros(1)+n
			self.lenn=1
			self.summ=1
      
    
	def printUF(self):
		print self.node
     
        
	def makeset(self, items):
		for it in range(len(items)):
			d=np.sum(items[it])
			s=int(''.join(map(str, items[it])),2)
			self.name[it]= (d, s)          # sum of '1' and decimal #
			self.node[it]=np.array(items[it])
			#self.summ[it]=np.sum(items[it])
		#self.clusters.append([1, parent, node])

        
	def find(self, node):
		return self.parent[node]

    
	def union(self, nodeA, nodeB):
		pA=int(self.find(nodeA))
		pB=int(self.find(nodeB))
		neighborsA=np.flatnonzero(self.parent==self.parent[pA])
		neighborsB=np.flatnonzero(self.parent==self.parent[pB])       
		#print neighborsA, pA,  neighborsB, pB, 'neigh'
		newlen=self.lenn[nodeA]+self.len[nodeB]
		if pA!=pB:
			if self.lenn[pA]>=self.len[pB]:            
				for iB in neighborsB:
					self.parent[iB]=self.parent[pA]
					self.lenn[iB]=newlen
				for iA in neighborsA:
					self.lenn[iA]=newlen
			else:
				for iA in neighborsA:
					self.parent[iA]=self.parent[pB]
					self.lenn[iA]=newlen
				for iB in neighborsB:                    
					self.lenn[iB]=newlen


#uf=UnionFind(range(len(D)))
#uf.makeset(items)