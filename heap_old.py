from math import log


class Heap:				# min at root heap
	def __init__(self, ar=None):

		if type(ar)==type([]):
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
	
	
	
	


	
	def extract_root(self):
		l=len(self.ar)
		levels=int(log(l,2))  # number of levels in heap, first level is levels=0
		childindex1=1
		childindex2=2
		parentindex=0
		if l<3:
			raise ValueError("too small heap")
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