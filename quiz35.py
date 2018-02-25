import numpy as np
import os
def OBST(weights):
    n=len(weights)
    L=np.zeros([n,n])
    for s in range(n):
        for i in range(1, n-s+1):
            Pk=0
            a=[]
            a2=[]
            for r in range(i, i+s+1):
                if i>r-1 or r-1==0:
                    a.append(0)
                else: 
                    a.append(L[i-1][r-1-1])  #-1
                if r+1>i+s or r+1>n:
                    a2.append(0)
                else:
                    print r, i
                    a2.append(L[r+1-1][i+s-1])
                Pk+=weights[r-1]
            Z=[]
            for z in range(len(a)):
                Z.append(Pk+a[z]+a2[z])
            L[i-1][i+s-1]=min(Z)
            print L, i, s, a, a2, Pk, Z
            os.system('pause')
    return L
    
    
    
#if __name__=='__main--':    

weights=[0.05, 0.4, 0.08, .04, 0.1, 0.1, 0.23]
w=OBST(weights)
print w
