inputfile=open('PA21.txt',"rb");
#inputfile=open('test13.txt',"rb");
#import os
data=[]
m=0
for line in inputfile.readlines():
    line=line.strip()
    if len(line)>3:
        row=line.split(' ')
        row[0]=int(row[0])
        row[1]=int(row[1])
        row[2]=int(row[2])
        if m<row[2]: m=row[2]
        if len(data)<1:
            data=[(row[0], row[1], row[2])]
        else:
            data.append((row[0], row[1], row[2]))
    else: N=int(line)
inputfile.close()
#print data
L=sorted(data, key=lambda x: x[2] )
print L[:10]
#LI=range(501)
LI={}
for d in L:
    LI[((d[0],d[1]))]=d[2]
	
	
import numpy as np
class UnionFind:
	def __init__(self, n):
		if type(n)==type([]):
			self.node=np.zeros(len(n),dtype=int)#[0]*len(n)
			self.len=np.ones(len(n), dtype=int) #*len(n)
			self.parent=np.ones(len(n), dtype=int)
			for i in n:
				self.node[i]=i
				self.parent[i]=i
		else: 
			self.node=np.zeros(1)+n
			self.parent=np.zeros(1)+n
			self.len=1
      
    
	def printUF(self):
		print self.node
     
        
	def makeset(self, node):
		#node.parent=node.vertex
		parent=node
		self.clusters.append([1, parent, node])

        
	def find(self, node):
		return self.parent[node]

    
	def union(self, nodeA, nodeB):
		pA=int(self.find(nodeA))
		pB=int(self.find(nodeB))
		#neighborsA=np.flatnonzero(self.parent==self.parent[pA])
		neighborsA = [i for i,x in enumerate(self.parent) if x == self.parent[pA]]
		neighborsB = [i for i,x in enumerate(self.parent) if x == self.parent[pB]]
		
		
		#neighborsB=np.flatnonzero(self.parent==self.parent[pB])       
		#print neighborsA, pA,  neighborsB, pB, 'neigh'
		newlen=self.len[pA]+self.len[pB]
		if pA!=pB:
			for iB in neighborsB:
				#self.len[iB]=newlen
				for iA in neighborsA:
					#print iA, iB, 'i'
					#print self.len[pA], self.len[pB], 'len'
					if self.len[pA]>=self.len[pB]:
						self.parent[iB]=self.parent[pA]
					else:
						self.parent[iA]=self.parent[pB]
					self.len[iA]=newlen
					self.len[iB]=newlen
					
					
uf=UnionFind(range(N+1))

# putting nodes into clusters as per Kruskal's algo
lenn=99
while lenn>5:
    edge=L.pop(0)
    #print edge
    uf.union(edge[0], edge[1])
    lenn=len(np.unique(uf.parent))
    if lenn%10==0:
        print lenn, edge
		
# finding the min distance among clusters. Min of distances returned
def cldist(uf, LI):
    cl=np.unique(uf.parent)
    mdist=999999
    mL=[]
    for i in cl:
        for j in cl:
            if i!=j:
                ii=np.flatnonzero(uf.parent==i)
                jj=np.flatnonzero(uf.parent==j)
                cli=uf.node[ii]
                clj=uf.node[jj]
                for clii in cli:
                    for cljj in clj:
                        if (clii, cljj) in LI:
                            if mdist>LI[(clii, cljj)]:
                                mdist=LI[(clii, cljj)]
                                mL.append(mdist)
    return min(mL)
		
		
		
print cldist(uf, LI)