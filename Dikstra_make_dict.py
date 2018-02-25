from heap import *
import pickle

f=open('Dikstra.txt', 'rb')
D={}
for i in f.readlines():
	
	#print i
	d=i.split()
	key=int(d[0])
	d=d[1:]
	L=[]
	for k in d:
		s=k.split(',')
		t=(int(s[0]), int(s[1]))
		L.append(t)
	D[key]=Heap(L)
f.close()
print D[10]
#pickle.dump(D, open("Dikstra.p", "wb"))				#dict values are heaps from Dikstra.txt


	