

from UnionFind import *				
inputfile=open('PA21.txt',"rb");
#inputfile=open('test13.txt',"rb");
import os
data=[]
m=0
for line in inputfile.readlines():
    line=line.strip()
    if len(line)>0:
        row=line.split(' ')
        row[0]=int(row[0])
        row[1]=int(row[1])
        row[2]=int(row[2])
        if m<row[2]: m=row[2]
        if len(data)<1:
            data=[(row[0], row[1], row[2])]
        else:
            data.append((row[0], row[1], row[2]))
inputfile.close()
L=sorted(data, key=lambda x: x[2] )
print L[:10]

uf=UnionFind()
for i in range(1, 501):
    uf.makeset(i)

#uf.printUF()
u=0
while len(uf.clusters)>4:
	p=L[u][0]
	q=L[u][1]
	#print uf.find(p), uf.find(q)
	uf.union(p,q)
	#print L[u], p, q, uf.clusters[uf.find(p)[2]]
	u+=1
	#os.system('pause')
uf.printUF()