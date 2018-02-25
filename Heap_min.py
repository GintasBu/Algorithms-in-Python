from math import log

# min Heap

class Heap_min:				# min at root heap
	def __init__(self, ar=None):

		if type(ar)==type([]) :
			if type(ar[0])==type((0,0)):
				L=sorted(ar, key=lambda x: x[1])
			else:
				L=sorted(ar)
			l=len(L)
			ara=[]
			i=0
			while l>0:
				k=2**i
				ara=ara+L[:k]
				i+=1
				L=L[k:]
				l=len(L)
		else:
			ara=[ar]
		self.ar=ara

			
	def __str__(self):
		return str(self.ar)
		
		
	def insert(self, el):
		self.ar=self.ar+[el]
		l=len(self.ar)
		#from math import log
		levels=int(log(l,2))  # number of levels in heap, first level is levels=0
		childindex=l-1			# newly inserted node, child and leave
		for i in range(levels, 0, -1):
				
			parentindex=2**(i-1)-1+	(childindex+1-2**i)/2		# parent's sequential number (index+1) on the level above
			if type(el)==type((0,0)):
				parent=self.ar[parentindex][1]		
				child=self.ar[childindex][1]
				#parent=self.ar[parentindex][0]				# these two lines if first number of tuple is compared
				#child=self.ar[childindex][0]
				
			else:
				child=self.ar[childindex]
				parent=self.ar[parentindex]				#parent's node index
			if parent > child:
				self.ar[childindex], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex] 
				childindex=parentindex
			else:
				return self
				break 
	
	
	
	
	def extract_vertex(self, node):
		l=len(self.ar)
		if l<2:
			if self.ar[0][0]==node:
				self.ar.pop()
				return self
			else:
				return self
		elif l==2:
			if self.ar[0][0]==node:
				self.ar[0], self.ar[1]=self.ar[1], self.ar[0]
				self.ar.pop()
				return self
			elif self.ar[1][0]==node:
				self.ar.pop()
				return self
			else:
				return self
		else:		
			levels=int(log(l,2))  # number of levels in heap, first level is levels=0
			j=0
			for i in self.ar:
				if i[0]==node:
					#childindex1=j+1
					#childindex2=j+2
					parentindex=j
					break
				j+=1
			if 'parentindex' not in locals():
				return self
			else:
			
			#print parentindex, "here"
				if j>=1:
				#j=j-1
					jlevel=int(log(j,2))
					jseq=j-2**jlevel
					childindex1=2**(jlevel+1)+jseq*2
					childindex2=2**(jlevel+1)+jseq*2+1
				else:
					childindex1=1
					childindex2=2
			#print parentindex, childindex1, childindex2, j
			
				

			
				if childindex1>l-1:			# no childred
					self.ar[parentindex], self.ar[l-1]=self.ar[l-1],self.ar[parentindex]
					self.ar.pop()
					return self
				elif childindex1<l & childindex2>l-1:
					self.ar[parentindex], self.ar[childindex1]=self.ar[childindex1],self.ar[parentindex]
					self.ar[childindex1], self.ar[l-1]=self.ar[l-1],self.ar[childindex1]
					self.ar.pop()
					return self
				else:
					lj=levels-j
					for i in range(lj):
					#print "i", i
						if type(self.ar[0])==type((0,0)):
							k=1		# or k=0 of first tuple number is interested
							if self.ar[childindex1][k]<=self.ar[childindex2][k]:
								self.ar[childindex1], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex1]
								parentindex=childindex1
							else:
								self.ar[childindex2], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex2]
								parentindex=childindex2
						else:
							if self.ar[childindex1]<=self.ar[childindex2]:
								self.ar[childindex1], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex1]
								parentindex=childindex1
							else:
								self.ar[childindex2], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex2]
								parentindex=childindex2
						if parentindex*2+2<l:
							childindex1=parentindex*2+1
							childindex2=parentindex*2+2
					self.ar[l-1], self.ar[parentindex]=self.ar[parentindex], self.ar[l-1]
					self.ar.pop()
					return self

					
	def extract_edge(self, node):
		l=len(self.ar)
		if l<2:
			if self.ar[0]==node:
				self.ar.pop()
				return self
			else:
				return self
		elif l==2:
			if self.ar[0]==node:
				self.ar[0], self.ar[1]=self.ar[1], self.ar[0]
				self.ar.pop()
				return self
			elif self.ar[1]==node:
				self.ar.pop()
				return self
			else:
				return self
		else:		
			levels=int(log(l,2))  # number of levels in heap, first level is levels=0
			j=0
			for i in self.ar:
				if i==node:
					#childindex1=j+1
					#childindex2=j+2
					parentindex=j
					break
				j+=1
			if 'parentindex' not in locals():
				return self
			else:
	    
	
				childindex1=2*j+1 #childindex1=2**(jlevel+1)+jseq*2
				childindex2=2*j+2 #childindex2=2**(jlevel+1)+jseq*2+1

				
				if childindex1>l-1:			# no children
					self.ar[parentindex], self.ar[l-1]=self.ar[l-1],self.ar[parentindex]
					self.ar.pop()
					return self
				elif childindex1<=l-1 & childindex2>l-1:
					self.ar[parentindex], self.ar[childindex1]=self.ar[childindex1],self.ar[parentindex]
					self.ar[childindex1], self.ar[l-1]=self.ar[l-1],self.ar[childindex1]
					self.ar.pop()
					return self
				else:
					while childindex2<l-1:
						#lj=levels-j
						#for i in range(lj):
					#print "i", i
						if type(self.ar[0])==type((0,0)):
							k=1		# or k=0 of first tuple number is interested
							if self.ar[childindex1][k]<=self.ar[childindex2][k]:
								self.ar[childindex1], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex1]
								parentindex=childindex1
							else:
								self.ar[childindex2], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex2]
								parentindex=childindex2
						else:
							if self.ar[childindex1]<=self.ar[childindex2]:
								self.ar[childindex1], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex1]
								parentindex=childindex1
							else:
								self.ar[childindex2], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex2]
								parentindex=childindex2
							#if parentindex*2+2<l:
						childindex1=parentindex*2+1
						childindex2=parentindex*2+2
						if childindex1>l-1:			# no children
							self.ar[parentindex], self.ar[l-1]=self.ar[l-1],self.ar[parentindex]
							self.ar.pop()
							return self
							break
						elif childindex1<=l-1 & childindex2>l-1:
							self.ar[parentindex], self.ar[childindex1]=self.ar[childindex1],self.ar[parentindex]
							self.ar[childindex1], self.ar[l-1]=self.ar[l-1],self.ar[childindex1]
							self.ar.pop()
							return self
							break
					
						#self.ar[l-1], self.ar[parentindex]=self.ar[parentindex], self.ar[l-1]
						#self.ar.pop()
						#return self
	
	
	
	def extract_root(self):
		l=len(self.ar)
		if l<2:
			self.ar.pop()
			return self
		else:
			levels=int(log(l,2))  # number of levels in heap, first level is levels=0
			childindex1=1
			childindex2=2
			parentindex=0
			if l<3:
				self.ar[0], self.ar[1]=self.ar[1], self.ar[0]
				self.ar.pop()
				return self
			else:
				for i in range(levels):
					if type(self.ar[0])==type((0,0)):
						k=1		# or k=0 of first tuple number is interested
						if self.ar[childindex1][k]<=self.ar[childindex2][k]:
							self.ar[childindex1], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex1]
							parentindex=childindex1
						else:
							self.ar[childindex2], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex2]
							parentindex=childindex2
					else:
						if self.ar[childindex1]<=self.ar[childindex2]:
							self.ar[childindex1], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex1]
							parentindex=childindex1
						else:
							self.ar[childindex2], self.ar[parentindex]=self.ar[parentindex], self.ar[childindex2]
							parentindex=childindex2

					if parentindex*2+2<l:
						childindex1=parentindex*2+1
						childindex2=parentindex*2+2
				self.ar[l-1], self.ar[parentindex]=self.ar[parentindex], self.ar[l-1]
				self.ar.pop()
				return self