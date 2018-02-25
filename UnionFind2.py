import numpy as np
class UnionFind:
	def __init__(self, n):
		if type(n)==type([]):
			self.node=np.zeros(len(n))#[0]*len(n)
			self.len=np.ones(len(n)) #*len(n)
			self.parent=np.ones(len(n))
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
		neighborsA=np.flatnonzero(self.parent==self.parent[pA])
		neighborsB=np.flatnonzero(self.parent==self.parent[pB])       
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