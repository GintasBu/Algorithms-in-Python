
items25 = [map(float, x.split(' ')) for x in open('PA5.txt', 'r').read().split('\n')[0:-1]]

import matplotlib
import matplotlib.pyplot as plt


A=[]
B=[]
C=[]
u=1
N=items[0][0]
for i in items:
    if len(i)>1:
        A.append(i[0])
        B.append(i[1])
        C.append(u)
        u+=1
		


N=int(items[0][0])
labels = ['{0}'.format(i) for i in C]
plt.subplots_adjust(bottom = 0.1)
plt.subplots_adjust(bottom = 0.1)
plt.scatter(A, B, marker = 'o')
for label, x, y in zip(C, A, B):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.show()

import math
import numpy as np

def get_data_matr(items):
    A=[0]
    B=[0]
    N=int(items[0][0])
    
    NN=int(N+1)
    mat=np.zeros([NN,NN])+float('+inf')
	
    for i in items:
        
        if len(i)>1:
            A.append(i[0])
            B.append(i[1])
    for k in range(1,NN):
        for l in range(1,NN):
            mat[k,l]=round(math.sqrt((A[k]-A[l])**2+ (B[k]-B[l])**2),4)
    return mat


def get_data_dict(items):
    A=[0]
    B=[0]
    N=items[0][0]
    NN=int(N+1)
    data={} 
    for i in items:
        
        if len(i)>1:
            A.append(i[0])
            B.append(i[1])
    for k in range(1,NN):
        for l in range(k+1,NN):
            y=(k,l)
            #print y
            if y not in data:
                x=round(math.sqrt((A[k]-A[l])**2+ (B[k]-B[l])**2),4)
                data[y]=x
                #print x, y
    return data
	
#dist=get_data_dict(items)	
#distmat=get_data_matr(items)



import itertools

def create_setl(m, n, i):     # i=1, n total # of vertexes, m says how many to include. i is always in m
    L2=[]
    #append=L2.append
    nn=range(1, n+1)
    nn.remove(i)
    L=list(itertools.combinations(nn,m))
    for l in L:
        #print l
        L2.append([i,]+list(l))
    return L2
	
	
def get_data_tuple(items):
    A=[]
    B=[]
    N=int(items[0][0])
    NN=int(N+1)
    data=[]
    for i in items:
        
        if len(i)>1:
            A.append(i[0])
            B.append(i[1])
            data.append([0]*N)
    for k in range(N):
        x=[]
        for l in range(N):
            x.append(round(math.sqrt((A[k]-A[l])**2+ (B[k]-B[l])**2),2))
        data[k]=tuple(x)
    return tuple(data)
	
	
	
def create_set(m, n, i):     # i=1, n total # of vertexes, m says how many to include. i is always in m
    L2=[]
    #append=L2.append
    nn=range(1, n+1)
    nn.remove(i)
    L=list(itertools.combinations(nn,m))
    for l in L:
        #print l
        L2.append((i,)+l)
    return L2
	
	
#import copy 
import time

def tsp3new(items):						# by far fastest. A is a dictionary instead poof LL or np.array
    start=time.time()
    #global A2, A1, sets2, sets1, dist, index1, index2
    N=int(items[0][0])
    dist=get_data_tuple(items)
    sets1=create_set(1, N, 1)
    #A1=[tuple([0]*len(sets1))]
    #A1=map(partial(fsetA2, lset=len(sets1), A2=A1), range(N-1))
    #for i in range(N-1):
    #    A1.append([float('+inf')]*len(sets1))
    A1={}
    for set1x in sets1:
        A1[set1x]=[float('+inf')]*(N-1)
    
    
    
    
    #print A1
    for m in range(1, N):
        sets2=create_set(m, N, 1)
        i=0
        if m<2:
            t=[]
            for setx in sets2:
                j=setx[1]
                A1[setx][j-2]=dist[0][j-1]
                #i+=1
            #print A1
        else:
            #A2=[[float('+inf')]*len(sets2)]
            #map(partial(fsetA2, lset=len(sets2), A2=A2), range(N-1))
            #A2=tuple(A2)
            #print m, 'm', A2
            A2={}
            for set2x in sets2:
                A2[set2x]=[float('+inf')]*(N-1)
            
            print sets2[0], 'sets2[0]', len(sets2)
            #index2=sets2.index
            #index1=sets1.index
            #pool.map(funmap, sets2)
            #map(funmap, sets2)
        
            #del sets1
            
            
            
            #print sets2[0], 'sets2[0]', len(sets2)
            #index2=sets2.index
            #index1=sets1.index
            for setx in sets2:
             #   i2=index2(setx)
                for j in setx:
                    a=[]
                    append=a.append
                    if j!=1:
                        y=list(setx)
                        y.remove(j)
                        y=tuple(y)
                    #    #print j, y, sets1, A1
                     #   i1=index1(tuple(y))
                        for k in y:
                            if k==1: continue
                            #print y, k, j, setx, A1[y], A1[y][k-2]+dist[k-1][j-1]
                            append(A1[y][k-2]+dist[k-1][j-1])
                        A2[setx][j-2]=min(a)
                        #print a
            for z in A2:
                A2[z]=tuple(A2[z])
            del sets1
            sets1=sets2
            del sets2, A1
            A1=A2
        #print A1, 'A1'
    i=1
    a=[]
    V=A2.values()[0]
    
    for last in V:
        a.append(last+dist[0][i])
        i+=1
    print time.time()-start
    return (a, A2)



def tsp3(items):
    start=time.time()
    N=int(items[0][0])
    dist=get_data_dict(items)
    sets1=create_set(1, N, 1)
    A1=np.zeros([N,len(sets1)])+float('+inf')
    A1[0,:]=0

    for m in range(1, N):
        sets2=create_set(m, N, 1)
        i=0
        if m<2:
            for setx in sets2:
                j=setx[1]
                A1[j-1, i]=dist[1,j]
                i+=1
        else:
            A2=np.zeros([N, len(sets2)])+float('+inf')
            print sets2[0], 'sets2[0]', len(sets2)
            index2=sets2.index
            index1=sets1.index
            for setx in sets2:
                i2=index2(setx)
                for j in setx:
                    a=[]
                    append=a.append
                    if j!=1:
                        y=list(setx)
                        y.remove(j)
                        #print j, y, sets1
                        i1=index1(tuple(y))
                        for k in y:
                            if k==1: continue
                            append(A1[k-1, i1]+dist[(min(k,j), max(k,j))])
                        A2[j-1,i2]=min(a)
            del sets1
            sets1=sets2
            del sets2, A1
            A1=copy.deepcopy(A2)
    i=2
    a=[]
    for last in A2[1:]:
		w=dist[1, i]+last[0]
		a.append(w)
		i+=1
    print time.time()-start
    return [A2, a]
	
def tsp3mat(items):
    start=time.time()
    N=int(items[0][0])
    dist=get_data_matr(items)
    sets1=create_setl(1, N, 1)
    A1=np.zeros([N+1,len(sets1)])+float('+inf')
    A1[0,:]=0
    for m in range(1, N):
        sets2=create_setl(m, N, 1)
        i=0
        if m<2:
            for setx in sets2:
                j=setx[1]
                A1[j, i]=distmat[1,j]
                i+=1
        else:
            A2=np.zeros([N+1, len(sets2)])+float('+inf')
            print sets2[0], 'sets2[0]', len(sets2)
            for setx in sets2:
                for j in setx:
                    a=[]
                    if j!=1:
                        i2=sets2.index(setx)
                        y=copy.deepcopy(setx)
                        y.remove(j)
                        i1=sets1.index(y)

                        d=distmat[y,j]
                        x=A1[y,i1]+d
						
						#for k in y:
                        #    if k!=1:
                        #        d=dist[(min(k,j), max(k,j))]
                                #print d, 'd', A1[k-1, i1], 'A1[k-1, i1]'
                        #        x=A1[k-1, i1]+d
                        #        a.append(x)
                        #print x, 'x', setx, 'setx', y, 'y', j, 'j', i1, 'i1', d, 'd'
                        A2[j,i2]=round(min(x),4)
                        
						
						#print A2, 'A2', j-1, 'j-1', i2, 'i2'
            del sets1
            sets1=copy.deepcopy(sets2)
            del A1
            A1=copy.deepcopy(A2)
        #print sets2, 'sets2'
        #print A1, 'A1', m
    i=1
    a=[]
    for last in A2:
        if i>1:
           
            w=distmat[1, i-1]+last[0]
            a.append(w)
        i+=1
    print time.time()-start
    return a #min(a)
	
	

def tsp3map(items):
    start=time.time()
    N=int(items[0][0])
    dist=get_data_matr(items)
    sets1=create_setl(1, N, 1)
    A1=np.zeros([N+1,len(sets1)])+float('+inf')
    A1[0,:]=0
    for m in range(1, N):
        sets2=create_setl(m, N, 1)
        i=0
        if m<2:
            for setx in sets2:
                j=setx[1]
                A1[j, i]=distmat[1,j]
                i+=1
        else:
            A2=np.zeros([N+1, len(sets2)])+float('+inf')
            print sets2[0], 'sets2[0]', len(sets2)
            for setx in sets2:
                i2=sets2.index(setx)
                for j in setx:
                    a=[]
                    if j!=1:
                        #i2=sets2.index(setx)
                        y=copy.deepcopy(setx)
                        #y=setx
                        y.remove(j)
                        #setx=setx.remove(j)
                        i1=sets1.index(y)

                        #d=distmat[setx,j]
                        #x=np.add(A1[y,i1],distmat[y,j])
						
						#for k in y:
                        #    if k!=1:
                        #        d=dist[(min(k,j), max(k,j))]
                                #print d, 'd', A1[k-1, i1], 'A1[k-1, i1]'
                        #        x=A1[k-1, i1]+d
                        #        a.append(x)
                        #print x, 'x', setx, 'setx', y, 'y', j, 'j', i1, 'i1', d, 'd'
                        A2[j,i2]=min(np.add(A1[y,i1],distmat[y,j]))
                        
						
						#print A2, 'A2', j-1, 'j-1', i2, 'i2'
            del sets1
            sets1=sets2
            del A1, sets2
            A1=copy.deepcopy(A2)
        #print sets2, 'sets2'
        #print A1, 'A1', m
    i=1
    a=[]
    for last in A2:
        if i>1:
           
            w=distmat[1, i-1]+last[0]
            a.append(w)
        i+=1
    print time.time()-start
    return min(a)