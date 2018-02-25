f=open('PA62.txt', 'rb')
import os

from heap_max import *
from heap_min import *

m=0
Hlow=Heap_max()
Hhigh=Heap_min()
for line in f:
	n=int(line)
	if Hlow.ar[0]==None:
		if len(Hlow.ar)==1:
			Heap_max.insert(Hlow, n)
			Hlow.ar[0], Hlow.ar[1]=Hlow.ar[1], Hlow.ar[0]
			Heap_max.extract_root(Hlow)
			
	else:
		if n<Hlow.ar[0]:
			Heap_max.insert(Hlow, n)
		else:
			Heap_min.insert(Hhigh, n)
	
	if len(Hhigh.ar)==2:
		if Hhigh.ar[0]==None:
			Heap_min.extract_root(Hhigh)
	
	if len(Hlow.ar)-len(Hhigh.ar)>1:
		Heap_min.insert(Hhigh, Hlow.ar[0])
		Heap_max.extract_root(Hlow)
	if len(Hlow.ar)-len(Hhigh.ar)<-1:
		Heap_max.insert(Hlow, Hhigh.ar[0])
		Heap_min.extract_root(Hhigh)
	
	
	if len(Hhigh.ar)==1:
		if Hhigh.ar[0]==None:
			Heap_min.extract_root(Hhigh)
	
	if len(Hlow.ar)-len(Hhigh.ar)==1:
		m0=Hlow.ar[0]
	elif len(Hlow.ar)-len(Hhigh.ar)==-1:
		m0=Hhigh.ar[0]
	else: m0=Hlow.ar[0]
	
	m+=m0
	
	
			
	#print 'Hlow', Hlow.ar
	#print 'Hhigh', Hhigh.ar
print m
	#os.system("pause")
	
f.close()