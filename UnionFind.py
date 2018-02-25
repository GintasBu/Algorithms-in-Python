class UnionFind:
	def __init__(self, size=None, parent=None):
		self.clusters=[]     # after running becomes format: length, parent, list of vertexes
		#self.size=size
		#self.parent=parent
		#return [self.size, self.parent, self.clusters]
       
    
	def printUF(self):
		print self.clusters
        #for k in self.clusters:
			#print Node.str(k[0]), self.size
			#print k, k.size, k.parent
		#print self.size
        
        
	def makeset(self, node):
		#node.parent=node.vertex
		parent=node
		self.clusters.append([1, parent, [node]])

        
	def find(self, node):
		z=0
		y=0
		for k in self.clusters:
			for l in k[2]:
				if l==node:
					return (k[1], k[0], y)    #second element is length, third index in the list
					z=1
			y+=1
		if z==0:
			self.makeset(node)
			return (node, 1, len(self.clusters)-1)    #second element is length

	
	def union(self, nodeA, nodeB):
		clA=self.find(nodeA)
		clB=self.find(nodeB)
		if clA[0]!=clB[0]:
			#if clA[1]>=clB[1]:
			self.clusters[clA[2]][2]=self.clusters[clA[2]][2]+self.clusters[clB[2]][2]
			self.clusters[clA[2]][0]=self.clusters[clA[2]][0]+self.clusters[clB[2]][0]
			del self.clusters[clB[2]]
			#else: 
			#	self.clusters[clB[2]][2]=self.clusters[clA[2]][2]+self.clusters[clB[2]][2]
			#	self.clusters[clB[2]][0]=self.clusters[clA[2]][0]+self.clusters[clB[2]][0]
			#	del self.clusters[clA[2]]
				
				
