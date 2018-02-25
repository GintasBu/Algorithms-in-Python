from Heap_min import *

import os

inputfile=open('PA13.txt',"rb");
#inputfile=open('Primtest13b.txt',"rb");
# number of nodes is 500, number of edges 2184
import os
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
#print data
#for i in range(1,6):
#    l=data[i]
#    data[i]=Heap_min(l)
Dl={}
for i in range(1, 501):
    Dl[i]=False
Dl2={k: v for k, v in Dl.items() if v==False}

cost=0
s=1
cross=Heap_min(data[s])
#print cross.ar
while len(Dl2)>0:
    Dl[s]=True
    e=cross.ar[0]
    cross.extract_root()
    #print s, e, 'edge'
    if e[0] in data:
        cross0=data[e[0]]
        for j in cross0:
            if Dl[j[0]]==True:
                cross0.remove(j)
                #print 'already visited', j
        for l in cross0:
            cross.insert(l)    # do not use insert!! see PA13bnset.py for good version
    #print cross.ar, 'cross'
    qu=cross
    cost+=e[1]
    Dl[e[0]]=True
    #print qu.ar, Dl, cost
    #os.system('pause')
    Dl2={k: v for k, v in Dl.items() if v==False}
    if len(Dl2)<1:
        print cost, 'cost'
        break
    s=qu.ar[0][0]
    
    while Dl[s]==True:
        qu.extract_root()
        if len(qu.ar[0])>0:
			s=qu.ar[0][0]
        #print 'came here', s
	#print s, e, cost, cross, qu.ar
	#os.system('pause')
    #Dl2={k: v for k, v in Dl.items() if v==False}
#cost