from Heap_min import *

import os

#inputfile=open('PA13.txt',"rb");
inputfile=open('Primtest13.txt',"rb");
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
inputfile.close()
data
#for i in range(1,6):
#    l=data[i]
#    data[i]=Heap_min(l)
Dl={}
for i in range(1, 6):
    Dl[i]=False
Dl2={k: v for k, v in Dl.items() if v==False}

cost=0
cross=[]
s=1
while len(Dl2)>0:
    Dl[s]=True
    e=data[s][0] 
    #e=data[s].ar[0]
    if Dl[e[0]]==False:
        cost+=e[1]
    print s, e, 'edge'
    Dl[e[0]]=True
    data[s].extract_root()
    cross0=data[s].ar
    for j in cross0:
        if Dl[j[0]]==True:
            cross0.remove(j)
            print 'already visited', j
    cross=cross+cross0
    Dl2={k: v for k, v in Dl.items() if v==False}
    qu=Heap_min(cross)
    s=qu.ar[0][0]
    while Dl[s]==True:
        qu.extract_root()
        s=qu.ar[0][0]
        print 'came here', s
	print s, e, cost, cross, qu.ar
	os.system('pause')
#cost