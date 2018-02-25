inputfile=open('PA21.txt',"rb");						# good working solution for PA21
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
	
	
#import numpy as np
class UnionFind:
	def __init__(self, n):
		if type(n)==type([]):
			self.node=[0]*len(n)
			self.len=[1]*len(n)
			self.parent=[1]*len(n)
			for i in n:
				self.node[i]=i
				self.parent[i]=i
		else: 
			self.node=n
			self.parent=n
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
		neighborsA=[i for i, x in enumerate(self.parent) if x ==self.parent[pA]]
		neighborsB=[i for i, x in enumerate(self.parent) if x ==self.parent[pB]]      
		#print neighborsA, pA,  neighborsB, pB, 'neigh'
		newlen=self.len[nodeA]+self.len[nodeB]
		if pA!=pB:
			if self.len[pA]>=self.len[pB]:            
				for iB in neighborsB:
					self.parent[iB]=self.parent[pA]
					self.len[iB]=newlen
				for iA in neighborsA:
					self.len[iA]=newlen
			else:
				for iA in neighborsA:
					self.parent[iA]=self.parent[pB]
					self.len[iA]=newlen
				for iB in neighborsB:                    
					self.len[iB]=newlen
					
uf=UnionFind(range(N+1))

# putting nodes into clusters as per Kruskal's algo
lenn=99
while lenn>5:
    edge=L.pop(0)
    #print edge
    uf.union(edge[0], edge[1])
    lenn=len(set(uf.parent))
    #if lenn%10==0:
    #    print lenn, edge
		
# finding the min distance among clusters. Min of distances returned
def cldist2(uf, LI):
    cl=set(uf.parent)
    mdist=999999
    mL=[]
    for i in cl:
        for j in cl:
            if i!=j:
                ii=[a for a,x in enumerate(uf.parent) if x == i]
                jj=[a for a,x in enumerate(uf.parent) if x == j]
                #print ii, jj

                for clii in range(len(ii)):#cli:
                    for cljj in range(len(jj)):
                        if (uf.node[ii[clii]], uf.node[jj[cljj]]) in LI:
                            if mdist>LI[(uf.node[ii[clii]], uf.node[jj[cljj]])]:
                                mdist=LI[(uf.node[ii[clii]], uf.node[jj[cljj]])]
                                mL.append(mdist)
    return min(mL)
		

print cldist2(uf, LI)