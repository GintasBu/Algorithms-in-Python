from Heap_min import *
import os
inputfile=open('PA13.txt',"rb");
#inputfile=open('Primtest13b.txt',"rb");
# number of nodes is 500, number of edges 2184
data={}
dd=inputfile.readline()
for line in inputfile.readlines():
    line=line.strip()
    if len(line)>0:
        row=line.split(' ')
        row[0]=int(row[0])
        row[1]=int(row[1])
        row[2]=int(row[2])
        if row[0] in data:
            data[row[0]]=data[row[0]] + [(row[1], row[2])]
        else:
            data[row[0]]=[(row[1], row[2])]
        if row[1] in data:
            data[row[1]]=data[row[1]] + [(row[0], row[2])]
        else:
            data[row[1]]=[(row[0], row[2])]	
			
inputfile.close()

Dl={}
for i in data:
    Dl[i]=False
#print data
cost=0
s=1
Dl[s]=True
cross=Heap_min(data[s])
while len(cross.ar)>0:
    e=cross.ar[0]
    cost+=e[1]
    Dl[e[0]]=True	
    cross0=data[e[0]]
    for l in cross0:
        cross.insert(l)
    toextract=[]
    for j in cross.ar:
        if Dl[j[0]]==True:
            toextract.append(j[0])
    for i in toextract:
        cross.extract_vertex(i)	
    print Dl, cross.ar
    os.system('pause')	
    print cost